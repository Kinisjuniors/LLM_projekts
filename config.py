
import os

INPUT_DIR = "input_files"
OUTPUT_DIR = "output_files"


GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
TEMPERATURE = float(os.getenv("GEMINI_TEMPERATURE", "0.3"))

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyAV4M8FSw3ynZiMYm3Hrc6K5g")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(INPUT_DIR, exist_ok=True)
