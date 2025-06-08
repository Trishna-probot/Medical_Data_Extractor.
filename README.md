# Medical_Data_Extractor.
Overview
This Python project extracts structured medical information from PDF documents such as patient medical reports and prescriptions. It automates the process of parsing unstructured text data and retrieving key fields including:

Patient Name

Age

Gender

Date of Report

Diagnosis keywords (e.g., fever, diabetes)

Medications (with dosage details)

Doctor’s Name

The extracted data is saved in both JSON and CSV formats for easy integration with downstream healthcare analytics, record keeping, or automated workflows.

Features
PDF Text Extraction: Utilizes PyMuPDF (fitz) for fast and accurate extraction of text from PDF files.

Natural Language Processing: Employs spaCy for entity recognition and enhanced text parsing.

Regex-Based Data Mining: Uses regular expressions for precise detection of names, dates, ages, genders, medications, and doctor details.

Diagnosis Identification: Searches for common diagnosis keywords within the text.

Multi-format Output: Exports results in both JSON and CSV formats for flexible data usage.

Extensible Architecture: Easily extendable to support OCR integration for scanned or handwritten documents.

