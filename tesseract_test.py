import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = Image.open('test_image.jpeg')

text = pytesseract.image_to_string(img)

print(text)


#Tells python where to find tesseract
#opens up the image
#uses AI to convert the image to text
#prints the text