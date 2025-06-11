# 🩺 MedExtract Pro – Intelligent Medical Data Extractor

**MedExtract Pro** is a lightweight, privacy-friendly tool built with **Flask**, **spaCy**, and **PyMuPDF** to extract meaningful patient information from medical reports (PDFs). Whether the report is typed or handwritten, the system intelligently detects and extracts names, dates, diagnosis, medications, and more — exporting the results to both **JSON** and **CSV** formats.

---

## ✨ Key Highlights

- ✅ Upload **PDF medical reports** (typed or scanned)
- 🧠 Uses **spaCy NLP** for intelligent entity extraction
- 🖼️ Integrated **OCR** with `pytesseract` for handwritten reports
- 📤 Exports to **JSON** and **CSV**
- 🧾 Professionally styled frontend with **Bootstrap**
- 🔐 Runs completely **locally** — no internet/data sharing required

---

## ⚙️ Tech Stack

| Layer      | Tools Used |
|------------|------------|
| Backend    | Flask, spaCy, PyMuPDF |
| Frontend   | HTML5, Bootstrap 5 |
| OCR Engine | pytesseract, pdf2image |
| Output     | JSON, CSV |

---

## 📁 Directory Structure

medical_data_extractor/

├── app.py                   # Main Flask app

├── extractor.py             # PDF reading and NLP logic

├── requirements.txt         # Required Python packages

├── vercel.json              # Optional config for Vercel (if deploying)

│
├── templates/               # HTML templates (for rendering pages)

│      ├── index.html           # Upload form page

│      └── result.html          # Extracted data display

│
|      ── static/                  # Static assets (CSS, JS, images)

│      └── logo.png             # App logo for navbar

│
├── uploads/                 # Uploaded PDF files (runtime)

│
├── output.json              # Latest extracted data in JSON

├── output.csv               # Latest extracted data in CSV

│
├── sample_medical.pdf       # Sample typed PDF for testing

│
└── README.md                # Project documentation (you’ll generate this now)

## Run the Flask App

python3 app.py

Then visit: http://127.0.0.1:5000

👩‍💻 Author
Trishna Kumari Paswan
