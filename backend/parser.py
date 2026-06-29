from pypdf import PdfReader
import os

# Folder containing PDF files
PDF_FOLDER = "../dataset/pdfs"

# Folder where extracted text will be saved
TEXT_FOLDER = "../dataset/text"

# Create text folder if it doesn't exist
os.makedirs(TEXT_FOLDER, exist_ok=True)

# Loop through all PDF files
for filename in os.listdir(PDF_FOLDER):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(PDF_FOLDER, filename)

        reader = PdfReader(pdf_path)
        text = ""

        # Read every page
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        # Save text with same filename
        text_filename = filename.replace(".pdf", ".txt")
        text_path = os.path.join(TEXT_FOLDER, text_filename)

        with open(text_path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"Extracted: {filename}")

print("✅ All PDFs processed successfully!")