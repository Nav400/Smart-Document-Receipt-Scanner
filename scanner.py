import cv2
import numpy as np

def process_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    denoised = cv2.fastNlMeansDenoising(gray)
    contrast = cv2.equalizeHist(denoised)

    return contrast

#processes image (turns the picture gray and brings contrast) and returns it to be read later

def detect_document(image):
    edges = cv2.Canny(image, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest = max(contours, key = cv2.contourArea)
        return largest
    return None

#identifies the image and finds the largest contour shape inside the picture (which is the content of the document) and returns that