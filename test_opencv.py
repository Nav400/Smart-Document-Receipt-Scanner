import cv2

img = cv2.imread('test_image.jpeg')
cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Load image from file
#Show it in a window
#Wait for you to press a key (this is what waitKey(0) does)
#Close the window (cleans up after you)