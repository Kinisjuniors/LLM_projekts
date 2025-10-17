
import os
import re
import json
import time
from typing import Optional
from config import INPUT_DIR, OUTPUT_DIR, GEMINI_MODEL, TEMPERATURE, GEMINI_API_KEY

try:
    
    from google import genai  
    CLIENT_STYLE = "google_genai"
except Exception:
    try:
        import google.generativeai as genai  
        CLIENT_STYLE = "google_generativeai"
    except Exception:
        genai = None
        CLIENT_STYLE = None

PROMPT_TEMPLATE_PATH = "prompts.md"


def init_client():
    if genai is None:
        raise RuntimeError(
            "Gen AI SDK not found. Install 'google-genai' (or 'google-generativeai' depending on docs)."
        )

    
    api_key = os.getenv("GEMINI_API_KEY") or GEMINI_API_KEY
    if not api_key:
        raise RuntimeError(
            "No GEMINI API key found. Set GEMINI_API_KEY environment variable or set GEMINI_API_KEY in config.py."
        )

    if CLIENT_STYLE == "google_genai":
        client = genai.Client(api_key=api_key)
        return client
    elif CLIENT_STYLE == "google_generativeai":
        genai.configure(api_key=api_key)
        return genai
    else:
        raise RuntimeError("Unsupported Gen AI client style.")


def build_prompt(jd_text: str, cv_text: str) -> str:
    tpl = ""
    if os.path.exists(PROMPT_TEMPLATE_PATH):
        tpl = open(PROMPT_TEMPLATE_PATH, "r", encoding="utf-8").read()
    else:
        tpl = open(PROMPT_TEMPLATE_PATH, "w", encoding="utf-8").write("")  
        tpl = (
            "You are an HR assistant. Produce JSON with fields: match_score, summary, strengths, missing_requirements, verdict.\n\n"
            "---- JOB DESCRIPTION ----\n{JD}\n\n---- CANDIDATE CV ----\n{CV}\n"
        )
    
    if "{JD}" in tpl and "{CV}" in tpl:
        return tpl.replace("{JD}", jd_text).replace("{CV}", cv_text)
    else:
        return tpl + "\n\n---- JOB DESCRIPTION ----\n" + jd_text + "\n\n---- CANDIDATE CV ----\n" + cv_text


def extract_json_from_text(text: str) -> Optional[dict]:
    """
    Mēģina droši izvilkt JSON no modeļa atbildes.
    Atbalsta arī markdown blokus (```json ... ```), trūkstošas iekavas u.c. gadījumus.
    """
    import re, json

   
    text = re.sub(r"^```[a-zA-Z]*", "", text)
    text = re.sub(r"```$", "", text)
    text = text.strip()

    
    try:
        data = json.loads(text)
        if isinstance(data, dict):
            return data
    except Exception:
        pass

    
    brace_stack = []
    start = None
    for i, ch in enumerate(text):
        if ch == '{':
            if start is None:
                start = i
            brace_stack.append(ch)
        elif ch == '}':
            if brace_stack:
                brace_stack.pop()
                if not brace_stack and start is not None:
                    candidate = text[start:i + 1]
                    try:
                        return json.loads(candidate)
                    except Exception:
                        continue

    pattern = re.compile(r"\{[\s\S]*\}")
    matches = pattern.findall(text)
    for m in matches:
        try:
            cleaned = m.replace("```", "")
            cleaned = re.sub(r",\s*]", "]", cleaned)
            cleaned = re.sub(r",\s*}", "}", cleaned)
            return json.loads(cleaned)
        except Exception:
            continue

    
    return None




def call_gemini(client, prompt: str, temperature: float, model: str) -> str:
    """
    Call Gemini/Gen AI and return the raw text response.
    This supports two SDK styles detected at import.
    """
    if CLIENT_STYLE == "google_genai":
        resp = client.models.generate_content(
    model=model,
    contents=prompt,
    config={"temperature": temperature}
)

        
        text = getattr(resp, "text", None)
        if text is None:
            
            try:
                text = resp.output[0].content[0].text
            except Exception:
                text = str(resp)
        return text

    elif CLIENT_STYLE == "google_generativeai":
        try:
            resp = client.generate_content(model=model, contents=prompt, temperature=temperature)
            text = getattr(resp, "text", None) or str(resp)
            return text
        except Exception:
            try:
                resp = client.generate_text(model=model, prompt=prompt, temperature=temperature)
                return resp.text
            except Exception as e:
                raise

    else:
        raise RuntimeError("Unsupported client style")


def save_json_and_report(basename: str, result: dict):
    json_path = os.path.join(OUTPUT_DIR, f"{basename}.json")
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, ensure_ascii=False, indent=2)

    md_path = os.path.join(OUTPUT_DIR, f"{basename}_report.md")
    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write(f"# {basename} - CV match report\n\n")
        fh.write(f"**Match score:** {result.get('match_score')}%\n\n")
        fh.write(f"**Verdict:** {result.get('verdict')}\n\n")
        fh.write("## Summary\n")
        fh.write(result.get("summary", "") + "\n\n")
        fh.write("## Strengths\n")
        for s in result.get("strengths", []):
            fh.write(f"- {s}\n")
        fh.write("\n## Missing requirements\n")
        for m in result.get("missing_requirements", []):
            fh.write(f"- {m}\n")


def run():
    client = init_client()

    
    jd_path = os.path.join(INPUT_DIR, "jd.txt")
    if not os.path.exists(jd_path):
        raise FileNotFoundError(f"Job description not found: {jd_path}")

    jd_text = open(jd_path, "r", encoding="utf-8").read()

    
    for i in range(1, 4):
        cv_filename = f"cv{i}.txt"
        cv_path = os.path.join(INPUT_DIR, cv_filename)
        if not os.path.exists(cv_path):
            print(f"Skipping {cv_filename} - file not found.")
            continue
        cv_text = open(cv_path, "r", encoding="utf-8").read()

        prompt = build_prompt(jd_text, cv_text)

        with open(PROMPT_TEMPLATE_PATH, "w", encoding="utf-8") as f:
            f.write(prompt)

        raw = None
        parsed = None

        for attempt in range(1, 4):
            try:
                raw = call_gemini(client, prompt, TEMPERATURE, GEMINI_MODEL)
            except Exception as e:
                print(f"Call to Gemini failed (attempt {attempt}): {e}")
                time.sleep(1)
                continue

            if not raw:
                print("Empty response, retrying...")
                time.sleep(0.5)
                continue

            parsed = extract_json_from_text(raw)
            if parsed and isinstance(parsed, dict):
                
                try:
                    parsed["match_score"] = int(parsed.get("match_score", 0))
                except Exception:
                    parsed["match_score"] = 0
                parsed.setdefault("summary", "")
                parsed.setdefault("strengths", [])
                parsed.setdefault("missing_requirements", [])
                parsed.setdefault("verdict", "possible match")
                break
            else:
                print(f"Attempt {attempt}: could not parse JSON. Model raw output preview:\n{raw[:500]}")
                time.sleep(0.8)

        if parsed is None:
            
            parsed = {
                "match_score": 0,
                "summary": "No valid JSON returned by model.",
                "strengths": [],
                "missing_requirements": [],
                "verdict": "not a match"
            }

        base = f"cv{i}"
        save_json_and_report(base, parsed)
        print(f"Saved {base}.json and {base}_report.md")

    print("All done. Check the output_files directory.")


if __name__ == "__main__":
    run()
