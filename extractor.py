import fitz  # PyMuPDF
import spacy
import re
import json
import pandas as pd

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path):
    """Extract text from each page of the PDF."""
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_data_with_spacy(text):
    """Extract structured medical data from unstructured text."""
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

    # Basic regex-based extraction
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

    # Search for medications
    for line in text.split('\n'):
        if re.search(r'\d+mg|\d+ ml|Tablet|Capsule|Injection', line, re.IGNORECASE):
            extracted["Medications"].append(line.strip())

    # Doctor name
    doc_match = re.search(r"Dr\.?\s+\w+\s*\w*", text)
    if doc_match:
        extracted["Doctor"] = doc_match.group(0)

    # Basic diagnosis keyword search
    keywords = ['fever', 'infection', 'pain', 'diabetes', 'hypertension', 'cancer']
    for keyword in keywords:
        if keyword in text.lower():
            extracted["Diagnosis"].append(keyword)

    return extracted

def save_data(extracted_data):
    """Save the data to both JSON and CSV formats."""
    with open("output/output.json", "w") as f:
        json.dump(extracted_data, f, indent=4)
    pd.DataFrame([extracted_data]).to_csv("output/output.csv", index=False)
