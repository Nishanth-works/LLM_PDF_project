from PyPDF2 import PdfReader
import logging

logging.basicConfig(level=logging.INFO)

def extract_text_from_pdf(pdf):
    raw_text = ''
    try:
        reader = PdfReader(pdf)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                raw_text += text + "\n"
        logging.info("PDF text extraction completed.")
    except Exception as e:
        logging.error(f"Error in extracting text from PDF: {e}")
    return raw_text