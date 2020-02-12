'''
from PIL import Image

img = Image.open('G://QzoneAutoOut//1.jpg')
img = img.convert("L")
img.save('G://QzoneAutoOut//3.jpg')

img = Image.open('G://QzoneAutoOut//2.png')
img = img.convert("L")
img = img.crop((39, 39, 93, 93))
img.save('G://QzoneAutoOut//4.png')

'''

import cv2
import numpy

img = cv2.imread('G://QzoneAutoOut//1.jpg');
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('G://QzoneAutoOut//3.jpg', gray)

img2 = cv2.imread('G://QzoneAutoOut//2.png');
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
gray2 = gray2[41:95, 41:95]
cv2.imwrite('G://QzoneAutoOut//4.jpg', gray2)

res = cv2.matchTemplate(gray, gray2, cv2.TM_CCOEFF_NORMED)
print(cv2.minMaxLoc(res)[3][0])
