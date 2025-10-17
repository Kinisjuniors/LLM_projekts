# AI darbināts CV vērtētājs (reāla Gemini integrācija)

## Kas šī ir?
Šī Python programma salīdzina vienu darba aprakstu (`jd.txt`) ar trīs kandidātu CV (`cv1.txt`–`cv3.txt`) un izmanto Google Gemini (Generative AI) API, lai ģenerētu HR-fokusa JSON rezultātu un Markdown pārskatu.

## Priekšnosacījumi
1. Python 3.10+ (rekomendēts)
2. Uzstādīt Google Gen AI Python SDK. Atkarības, piemērs:
```bash
pip install google-genai
