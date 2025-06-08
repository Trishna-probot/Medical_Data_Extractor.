import fitz  # PyMuPDF
import spacy
import re
import json
import pandas as pd

# Load NLP model
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_medical_data(text):
    doc = nlp(text)
    extracted = {
        "Name": None,
        "Age": None,
        "Gender": None,
        "Date": None,
        "Diagnosis": [],
        "Medications": [],
        "Doctor": None
    }

    name = re.search(r"Name[:\-]?\s*(\w+\s*\w+)", text)
    if name:
        extracted["Name"] = name.group(1)

    age = re.search(r"Age[:\-]?\s*(\d+)", text)
    if age:
        extracted["Age"] = age.group(1)

    gender = re.search(r"Gender[:\-]?\s*(Male|Female|Other)", text, re.IGNORECASE)
    if gender:
        extracted["Gender"] = gender.group(1)

    date = re.search(r"Date[:\-]?\s*([\d/.\-]+)", text)
    if date:
        extracted["Date"] = date.group(1)

    for line in text.split('\n'):
        if re.search(r'\d+mg|\d+ ml|Tablet|Capsule|Injection', line, re.IGNORECASE):
            extracted["Medications"].append(line.strip())

    doc_match = re.search(r"Dr\.?\s+\w+\s*\w*", text)
    if doc_match:
        extracted["Doctor"] = doc_match.group(0)

    keywords = ['fever', 'infection', 'pain', 'diabetes', 'hypertension', 'cancer']
    for keyword in keywords:
        if keyword in text.lower():
            extracted["Diagnosis"].append(keyword)

    return extracted

def save_data(extracted_data):
    with open("output.json", "w") as f:
        json.dump(extracted_data, f, indent=4)
    pd.DataFrame([extracted_data]).to_csv("output.csv", index=False)

if __name__ == "__main__":
    text = extract_text_from_pdf("sample_medical.pdf")
    data = extract_medical_data(text)
    save_data(data)
    print("✅ Extraction complete! Output saved in output.json and output.csv")
