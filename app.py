
from flask import Flask, request, render_template
import os
from extractor import extract_text_from_pdf, extract_data_with_spacy
import csv
import json

app = Flask(__name__, static_folder="static", template_folder="templates")

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "pdf" not in request.files:
            return "No file part in the request"

        file = request.files["pdf"]

        if file.filename == "":
            return "No selected file"

        filename = file.filename.replace(" ", "_")
        path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(path)

        if os.path.getsize(path) == 0:
            return "Uploaded file is empty."

        try:
            text = extract_text_from_pdf(path)
            data = extract_data_with_spacy(text)

            with open("output.json", "w") as json_file:
                json.dump(data, json_file, indent=4)

            with open("output.csv", "w", newline="") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=data.keys())
                writer.writeheader()
                writer.writerow(data)

            return render_template("result.html", data=data)

        except Exception as e:
            return f"An error occurred: {str(e)}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
