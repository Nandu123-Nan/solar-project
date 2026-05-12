import re
import pytesseract
from pdf2image import convert_from_path

def extract_text_from_pdf(pdf_path):

    text = ""

    # Convert PDF pages into images
    pages = convert_from_path(pdf_path)

    for page in pages:

        extracted_text = pytesseract.image_to_string(page)

        text += extracted_text

    return text


def extract_bill_data(text):

    data = {}

    # Find units consumed
    units = re.search(r'18292\s+1\.00\s+(\d+)', text)

    if units:
        data['units'] = units.group(1)
    else:
        data['units'] = "Not Found"

    # Find bill amount
    amount = re.search(r'Rs\.?\s*(\d+)', text)

    if amount:
        data['amount'] = amount.group(1)
    else:
        data['amount'] = "Not Found"

    return data
