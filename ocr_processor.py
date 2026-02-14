import pytesseract
from PIL import Image
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

def extract_amounts(text):
    pattern = r'\$?\d+\.\d{2}|\$?\d+'
    amounts = re.findall(pattern, text)
    cleaned = [float(amt.replace('$', '')) for amt in amounts]
    return cleaned

def extract_date(text):
    date_pattern = r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}'
    dates = re.findall(date_pattern, text)
    return dates[0] if dates else 'Unknown'

#takes the image and gets the text out of it, then takes out the dollar amounts and formats them, then takes out the date they occurred on
