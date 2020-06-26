import pytesseract
from PIL import Image
import cv2

img = cv2.imread('Image Name',cv2.IMREAD_COLOR) #Open the image from which charectors has to be recognized
#img = cv2.resize(img, (620,480) ) #resize the image if required

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey to reduce detials
gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise

original = pytesseract.image_to_string(gray, config='')
#test = (pytesseract.image_to_data(gray, lang=None, config='', nice=0) ) #get confidence level if required
#print(pytesseract.image_to_boxes(gray))

print (original)
