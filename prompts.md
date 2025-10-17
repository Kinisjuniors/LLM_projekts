# Prompt template for Gemini (HR-focused, request JSON)

You are an HR assistant. Compare the following Job Description (JD) and a single Candidate CV.
Return ONLY valid JSON (no extra commentary), matching this exact schema:

{
  "match_score": 0-100,                      // integer 0..100
  "summary": "Short summary of how well the CV fits the JD.",
  "strengths": ["list", "of", "matched", "skills/experience"],
  "missing_requirements": ["list", "of", "important", "JD", "requirements", "not", "found", "in", "CV"],
  "verdict": "strong match | possible match | not a match"
}

Instructions:
- Use the JD and CV text below to compute match_score (0-100).
- Keep summary concise (1–3 sentences).
- Make strengths and missing_requirements specific and short.
- Choose verdict based on match_score and content.
- Temperature should be low (<= 0.3) for stability.
- Output must be valid JSON. If the model is uncertain, pick "possible match".

---- JOB DESCRIPTION ----
Darba apraksts: Python izstrādātājs

Meklējam Python izstrādātāju ar pieredzi tīmekļa lietotņu un datu apstrādes risinājumu izstrādē.
Galvenie pienākumi:
- API un backend funkcionalitātes izstrāde (Flask vai FastAPI)
- Datu apstrāde un integrācija ar SQL datubāzēm
- Sadarbība ar frontend izstrādātājiem un projektu vadītājiem
- Koda versēšana ar Git

Prasības:
- Vismaz 2 gadu pieredze Python izstrādē
- Zināšanas par REST API, Git un SQL
- Vēlams pieredze ar Docker un CI/CD
- Spēja strādāt komandā un komunicēt ar kolēģiem


---- CANDIDATE CV ----
Kandidāts: Jānis Ozoliņš

Pieredze:
Python izstrādātājs uzņēmumā DataLabs (2021–2024)
- Izstrādāju REST API ar Flask un FastAPI
- Strādāju ar PostgreSQL un MySQL datubāzēm
- Automatizēju datu apstrādes procesus (Pandas, NumPy)
- Lietoju Git un Docker komandas darbam

Papildu prasmes:
- Pieredze ar CI/CD (GitHub Actions)
- Laba komandas sadarbība
- Interese par mašīnmācīšanos



---- JOB DESCRIPTION ----
Darba apraksts: Python izstrādātājs

Meklējam Python izstrādātāju ar pieredzi tīmekļa lietotņu un datu apstrādes risinājumu izstrādē.
Galvenie pienākumi:
- API un backend funkcionalitātes izstrāde (Flask vai FastAPI)
- Datu apstrāde un integrācija ar SQL datubāzēm
- Sadarbība ar frontend izstrādātājiem un projektu vadītājiem
- Koda versēšana ar Git

Prasības:
- Vismaz 2 gadu pieredze Python izstrādē
- Zināšanas par REST API, Git un SQL
- Vēlams pieredze ar Docker un CI/CD
- Spēja strādāt komandā un komunicēt ar kolēģiem


---- CANDIDATE CV ----
Kandidāte: Līga Kalniņa

Pieredze:
DevOps un sistēmu administrators (2020–2024)
- Darbs ar Docker, Jenkins un CI/CD cauruļvadiem
- Python izmantoju skriptu automatizācijai
- Uzturēju Linux serverus un uzraudzības risinājumus
- Pieredze ar Git un Bash skriptiem

Papildu prasmes:
- AWS un Kubernetes pamatzināšanas
- Komandas darba pieredze IT infrastruktūras projektos
- Interese par backend izstrādi


---- JOB DESCRIPTION ----
Darba apraksts: Python izstrādātājs

Meklējam Python izstrādātāju ar pieredzi tīmekļa lietotņu un datu apstrādes risinājumu izstrādē.
Galvenie pienākumi:
- API un backend funkcionalitātes izstrāde (Flask vai FastAPI)
- Datu apstrāde un integrācija ar SQL datubāzēm
- Sadarbība ar frontend izstrādātājiem un projektu vadītājiem
- Koda versēšana ar Git

Prasības:
- Vismaz 2 gadu pieredze Python izstrādē
- Zināšanas par REST API, Git un SQL
- Vēlams pieredze ar Docker un CI/CD
- Spēja strādāt komandā un komunicēt ar kolēģiem


---- CANDIDATE CV ----
Kandidāts: Mārtiņš Bērziņš

Izglītība:
Rīgas Tehniskā universitāte, Datorzinātne (2020–2024)
Bakalaura darbs par Python datu analīzes risinājumiem.

Pieredze:
- Universitātes projekti ar Flask un SQLite
- Veidoju mazas tīmekļa lietotnes un datu analīzes skriptus
- Prakses laikā palīdzēju komandai veidot API dokumentāciju

Papildu prasmes:
- Python, SQL, HTML/CSS
- Laba motivācija un vēlme mācīties jaunas tehnoloģijas
- Nav vēl pieredzes ar Docker un CI/CD


---- JOB DESCRIPTION ----
Darba apraksts: Python izstrādātājs

Meklējam Python izstrādātāju ar pieredzi tīmekļa lietotņu un datu apstrādes risinājumu izstrādē.
Galvenie pienākumi:
- API un backend funkcionalitātes izstrāde (Flask vai FastAPI)
- Datu apstrāde un integrācija ar SQL datubāzēm
- Sadarbība ar frontend izstrādātājiem un projektu vadītājiem
- Koda versēšana ar Git

Prasības:
- Vismaz 2 gadu pieredze Python izstrādē
- Zināšanas par REST API, Git un SQL
- Vēlams pieredze ar Docker un CI/CD
- Spēja strādāt komandā un komunicēt ar kolēģiem


---- CANDIDATE CV ----
Kandidāts: Jānis Ozoliņš

Pieredze:
Python izstrādātājs uzņēmumā DataLabs (2021–2024)
- Izstrādāju REST API ar Flask un FastAPI
- Strādāju ar PostgreSQL un MySQL datubāzēm
- Automatizēju datu apstrādes procesus (Pandas, NumPy)
- Lietoju Git un Docker komandas darbam

Papildu prasmes:
- Pieredze ar CI/CD (GitHub Actions)
- Laba komandas sadarbība
- Interese par mašīnmācīšanos


---- JOB DESCRIPTION ----
Darba apraksts: Python izstrādātājs

Meklējam Python izstrādātāju ar pieredzi tīmekļa lietotņu un datu apstrādes risinājumu izstrādē.
Galvenie pienākumi:
- API un backend funkcionalitātes izstrāde (Flask vai FastAPI)
- Datu apstrāde un integrācija ar SQL datubāzēm
- Sadarbība ar frontend izstrādātājiem un projektu vadītājiem
- Koda versēšana ar Git

Prasības:
- Vismaz 2 gadu pieredze Python izstrādē
- Zināšanas par REST API, Git un SQL
- Vēlams pieredze ar Docker un CI/CD
- Spēja strādāt komandā un komunicēt ar kolēģiem


---- CANDIDATE CV ----
Kandidāte: Līga Kalniņa

Pieredze:
DevOps un sistēmu administrators (2020–2024)
- Darbs ar Docker, Jenkins un CI/CD cauruļvadiem
- Python izmantoju skriptu automatizācijai
- Uzturēju Linux serverus un uzraudzības risinājumus
- Pieredze ar Git un Bash skriptiem

Papildu prasmes:
- AWS un Kubernetes pamatzināšanas
- Komandas darba pieredze IT infrastruktūras projektos
- Interese par backend izstrādi


---- JOB DESCRIPTION ----
Darba apraksts: Python izstrādātājs

Meklējam Python izstrādātāju ar pieredzi tīmekļa lietotņu un datu apstrādes risinājumu izstrādē.
Galvenie pienākumi:
- API un backend funkcionalitātes izstrāde (Flask vai FastAPI)
- Datu apstrāde un integrācija ar SQL datubāzēm
- Sadarbība ar frontend izstrādātājiem un projektu vadītājiem
- Koda versēšana ar Git

Prasības:
- Vismaz 2 gadu pieredze Python izstrādē
- Zināšanas par REST API, Git un SQL
- Vēlams pieredze ar Docker un CI/CD
- Spēja strādāt komandā un komunicēt ar kolēģiem


---- CANDIDATE CV ----
Kandidāts: Mārtiņš Bērziņš

Izglītība:
Rīgas Tehniskā universitāte, Datorzinātne (2020–2024)
Bakalaura darbs par Python datu analīzes risinājumiem.

Pieredze:
- Universitātes projekti ar Flask un SQLite
- Veidoju mazas tīmekļa lietotnes un datu analīzes skriptus
- Prakses laikā palīdzēju komandai veidot API dokumentāciju

Papildu prasmes:
- Python, SQL, HTML/CSS
- Laba motivācija un vēlme mācīties jaunas tehnoloģijas
- Nav vēl pieredzes ar Docker un CI/CD


---- JOB DESCRIPTION ----
Darba apraksts: Python izstrādātājs

Meklējam Python izstrādātāju ar pieredzi tīmekļa lietotņu un datu apstrādes risinājumu izstrādē.
Galvenie pienākumi:
- API un backend funkcionalitātes izstrāde (Flask vai FastAPI)
- Datu apstrāde un integrācija ar SQL datubāzēm
- Sadarbība ar frontend izstrādātājiem un projektu vadītājiem
- Koda versēšana ar Git

Prasības:
- Vismaz 2 gadu pieredze Python izstrādē
- Zināšanas par REST API, Git un SQL
- Vēlams pieredze ar Docker un CI/CD
- Spēja strādāt komandā un komunicēt ar kolēģiem


---- CANDIDATE CV ----
Kandidāts: Jānis Ozoliņš

Pieredze:
Python izstrādātājs uzņēmumā DataLabs (2021–2024)
- Izstrādāju REST API ar Flask un FastAPI
- Strādāju ar PostgreSQL un MySQL datubāzēm
- Automatizēju datu apstrādes procesus (Pandas, NumPy)
- Lietoju Git un Docker komandas darbam

Papildu prasmes:
- Pieredze ar CI/CD (GitHub Actions)
- Laba komandas sadarbība
- Interese par mašīnmācīšanos


---- JOB DESCRIPTION ----
Darba apraksts: Python izstrādātājs

Meklējam Python izstrādātāju ar pieredzi tīmekļa lietotņu un datu apstrādes risinājumu izstrādē.
Galvenie pienākumi:
- API un backend funkcionalitātes izstrāde (Flask vai FastAPI)
- Datu apstrāde un integrācija ar SQL datubāzēm
- Sadarbība ar frontend izstrādātājiem un projektu vadītājiem
- Koda versēšana ar Git

Prasības:
- Vismaz 2 gadu pieredze Python izstrādē
- Zināšanas par REST API, Git un SQL
- Vēlams pieredze ar Docker un CI/CD
- Spēja strādāt komandā un komunicēt ar kolēģiem


---- CANDIDATE CV ----
Kandidāte: Līga Kalniņa

Pieredze:
DevOps un sistēmu administrators (2020–2024)
- Darbs ar Docker, Jenkins un CI/CD cauruļvadiem
- Python izmantoju skriptu automatizācijai
- Uzturēju Linux serverus un uzraudzības risinājumus
- Pieredze ar Git un Bash skriptiem

Papildu prasmes:
- AWS un Kubernetes pamatzināšanas
- Komandas darba pieredze IT infrastruktūras projektos
- Interese par backend izstrādi


---- JOB DESCRIPTION ----
Darba apraksts: Python izstrādātājs

Meklējam Python izstrādātāju ar pieredzi tīmekļa lietotņu un datu apstrādes risinājumu izstrādē.
Galvenie pienākumi:
- API un backend funkcionalitātes izstrāde (Flask vai FastAPI)
- Datu apstrāde un integrācija ar SQL datubāzēm
- Sadarbība ar frontend izstrādātājiem un projektu vadītājiem
- Koda versēšana ar Git

Prasības:
- Vismaz 2 gadu pieredze Python izstrādē
- Zināšanas par REST API, Git un SQL
- Vēlams pieredze ar Docker un CI/CD
- Spēja strādāt komandā un komunicēt ar kolēģiem


---- CANDIDATE CV ----
Kandidāts: Mārtiņš Bērziņš

Izglītība:
Rīgas Tehniskā universitāte, Datorzinātne (2020–2024)
Bakalaura darbs par Python datu analīzes risinājumiem.

Pieredze:
- Universitātes projekti ar Flask un SQLite
- Veidoju mazas tīmekļa lietotnes un datu analīzes skriptus
- Prakses laikā palīdzēju komandai veidot API dokumentāciju

Papildu prasmes:
- Python, SQL, HTML/CSS
- Laba motivācija un vēlme mācīties jaunas tehnoloģijas
- Nav vēl pieredzes ar Docker un CI/CD


---- JOB DESCRIPTION ----
Darba apraksts: Python izstrādātājs

Meklējam Python izstrādātāju ar pieredzi tīmekļa lietotņu un datu apstrādes risinājumu izstrādē.
Galvenie pienākumi:
- API un backend funkcionalitātes izstrāde (Flask vai FastAPI)
- Datu apstrāde un integrācija ar SQL datubāzēm
- Sadarbība ar frontend izstrādātājiem un projektu vadītājiem
- Koda versēšana ar Git

Prasības:
- Vismaz 2 gadu pieredze Python izstrādē
- Zināšanas par REST API, Git un SQL
- Vēlams pieredze ar Docker un CI/CD
- Spēja strādāt komandā un komunicēt ar kolēģiem


---- CANDIDATE CV ----
Kandidāts: Jānis Ozoliņš

Pieredze:
Python izstrādātājs uzņēmumā DataLabs (2021–2024)
- Izstrādāju REST API ar Flask un FastAPI
- Strādāju ar PostgreSQL un MySQL datubāzēm
- Automatizēju datu apstrādes procesus (Pandas, NumPy)
- Lietoju Git un Docker komandas darbam

Papildu prasmes:
- Pieredze ar CI/CD (GitHub Actions)
- Laba komandas sadarbība
- Interese par mašīnmācīšanos


---- JOB DESCRIPTION ----
Darba apraksts: Python izstrādātājs

Meklējam Python izstrādātāju ar pieredzi tīmekļa lietotņu un datu apstrādes risinājumu izstrādē.
Galvenie pienākumi:
- API un backend funkcionalitātes izstrāde (Flask vai FastAPI)
- Datu apstrāde un integrācija ar SQL datubāzēm
- Sadarbība ar frontend izstrādātājiem un projektu vadītājiem
- Koda versēšana ar Git

Prasības:
- Vismaz 2 gadu pieredze Python izstrādē
- Zināšanas par REST API, Git un SQL
- Vēlams pieredze ar Docker un CI/CD
- Spēja strādāt komandā un komunicēt ar kolēģiem


---- CANDIDATE CV ----
Kandidāte: Līga Kalniņa

Pieredze:
DevOps un sistēmu administrators (2020–2024)
- Darbs ar Docker, Jenkins un CI/CD cauruļvadiem
- Python izmantoju skriptu automatizācijai
- Uzturēju Linux serverus un uzraudzības risinājumus
- Pieredze ar Git un Bash skriptiem

Papildu prasmes:
- AWS un Kubernetes pamatzināšanas
- Komandas darba pieredze IT infrastruktūras projektos
- Interese par backend izstrādi


---- JOB DESCRIPTION ----
Darba apraksts: Python izstrādātājs

Meklējam Python izstrādātāju ar pieredzi tīmekļa lietotņu un datu apstrādes risinājumu izstrādē.
Galvenie pienākumi:
- API un backend funkcionalitātes izstrāde (Flask vai FastAPI)
- Datu apstrāde un integrācija ar SQL datubāzēm
- Sadarbība ar frontend izstrādātājiem un projektu vadītājiem
- Koda versēšana ar Git

Prasības:
- Vismaz 2 gadu pieredze Python izstrādē
- Zināšanas par REST API, Git un SQL
- Vēlams pieredze ar Docker un CI/CD
- Spēja strādāt komandā un komunicēt ar kolēģiem


---- CANDIDATE CV ----
Kandidāts: Mārtiņš Bērziņš

Izglītība:
Rīgas Tehniskā universitāte, Datorzinātne (2020–2024)
Bakalaura darbs par Python datu analīzes risinājumiem.

Pieredze:
- Universitātes projekti ar Flask un SQLite
- Veidoju mazas tīmekļa lietotnes un datu analīzes skriptus
- Prakses laikā palīdzēju komandai veidot API dokumentāciju

Papildu prasmes:
- Python, SQL, HTML/CSS
- Laba motivācija un vēlme mācīties jaunas tehnoloģijas
- Nav vēl pieredzes ar Docker un CI/CD


---- JOB DESCRIPTION ----
Darba apraksts: Python izstrādātājs

Meklējam Python izstrādātāju ar pieredzi tīmekļa lietotņu un datu apstrādes risinājumu izstrādē.
Galvenie pienākumi:
- API un backend funkcionalitātes izstrāde (Flask vai FastAPI)
- Datu apstrāde un integrācija ar SQL datubāzēm
- Sadarbība ar frontend izstrādātājiem un projektu vadītājiem
- Koda versēšana ar Git

Prasības:
- Vismaz 2 gadu pieredze Python izstrādē
- Zināšanas par REST API, Git un SQL
- Vēlams pieredze ar Docker un CI/CD
- Spēja strādāt komandā un komunicēt ar kolēģiem


---- CANDIDATE CV ----
Kandidāts: Jānis Ozoliņš

Pieredze:
Python izstrādātājs uzņēmumā DataLabs (2021–2024)
- Izstrādāju REST API ar Flask un FastAPI
- Strādāju ar PostgreSQL un MySQL datubāzēm
- Automatizēju datu apstrādes procesus (Pandas, NumPy)
- Lietoju Git un Docker komandas darbam

Papildu prasmes:
- Pieredze ar CI/CD (GitHub Actions)
- Laba komandas sadarbība
- Interese par mašīnmācīšanos


---- JOB DESCRIPTION ----
Darba apraksts: Python izstrādātājs

Meklējam Python izstrādātāju ar pieredzi tīmekļa lietotņu un datu apstrādes risinājumu izstrādē.
Galvenie pienākumi:
- API un backend funkcionalitātes izstrāde (Flask vai FastAPI)
- Datu apstrāde un integrācija ar SQL datubāzēm
- Sadarbība ar frontend izstrādātājiem un projektu vadītājiem
- Koda versēšana ar Git

Prasības:
- Vismaz 2 gadu pieredze Python izstrādē
- Zināšanas par REST API, Git un SQL
- Vēlams pieredze ar Docker un CI/CD
- Spēja strādāt komandā un komunicēt ar kolēģiem


---- CANDIDATE CV ----
Kandidāts: Jānis Ozoliņš

Pieredze:
Python izstrādātājs uzņēmumā DataLabs (2021–2024)
- Izstrādāju REST API ar Flask un FastAPI
- Strādāju ar PostgreSQL un MySQL datubāzēm
- Automatizēju datu apstrādes procesus (Pandas, NumPy)
- Lietoju Git un Docker komandas darbam

Papildu prasmes:
- Pieredze ar CI/CD (GitHub Actions)
- Laba komandas sadarbība
- Interese par mašīnmācīšanos


---- JOB DESCRIPTION ----
Darba apraksts: Python izstrādātājs

Meklējam Python izstrādātāju ar pieredzi tīmekļa lietotņu un datu apstrādes risinājumu izstrādē.
Galvenie pienākumi:
- API un backend funkcionalitātes izstrāde (Flask vai FastAPI)
- Datu apstrāde un integrācija ar SQL datubāzēm
- Sadarbība ar frontend izstrādātājiem un projektu vadītājiem
- Koda versēšana ar Git

Prasības:
- Vismaz 2 gadu pieredze Python izstrādē
- Zināšanas par REST API, Git un SQL
- Vēlams pieredze ar Docker un CI/CD
- Spēja strādāt komandā un komunicēt ar kolēģiem


---- CANDIDATE CV ----
Kandidāte: Līga Kalniņa

Pieredze:
DevOps un sistēmu administrators (2020–2024)
- Darbs ar Docker, Jenkins un CI/CD cauruļvadiem
- Python izmantoju skriptu automatizācijai
- Uzturēju Linux serverus un uzraudzības risinājumus
- Pieredze ar Git un Bash skriptiem

Papildu prasmes:
- AWS un Kubernetes pamatzināšanas
- Komandas darba pieredze IT infrastruktūras projektos
- Interese par backend izstrādi


---- JOB DESCRIPTION ----
Darba apraksts: Python izstrādātājs

Meklējam Python izstrādātāju ar pieredzi tīmekļa lietotņu un datu apstrādes risinājumu izstrādē.
Galvenie pienākumi:
- API un backend funkcionalitātes izstrāde (Flask vai FastAPI)
- Datu apstrāde un integrācija ar SQL datubāzēm
- Sadarbība ar frontend izstrādātājiem un projektu vadītājiem
- Koda versēšana ar Git

Prasības:
- Vismaz 2 gadu pieredze Python izstrādē
- Zināšanas par REST API, Git un SQL
- Vēlams pieredze ar Docker un CI/CD
- Spēja strādāt komandā un komunicēt ar kolēģiem


---- CANDIDATE CV ----
Kandidāts: Mārtiņš Bērziņš

Izglītība:
Rīgas Tehniskā universitāte, Datorzinātne (2020–2024)
Bakalaura darbs par Python datu analīzes risinājumiem.

Pieredze:
- Universitātes projekti ar Flask un SQLite
- Veidoju mazas tīmekļa lietotnes un datu analīzes skriptus
- Prakses laikā palīdzēju komandai veidot API dokumentāciju

Papildu prasmes:
- Python, SQL, HTML/CSS
- Laba motivācija un vēlme mācīties jaunas tehnoloģijas
- Nav vēl pieredzes ar Docker un CI/CD
