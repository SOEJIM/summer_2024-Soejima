import cv2
import numpy as np

img = cv2.imread("Resources/lambo.png")
print(img.shape)

imgResize = cv2.resize(img,(200,100))

imgCropped = img[0:200,200:500]

cv2.imshow("Output",img)
cv2.imshow("Resized Output",imgResize)
cv2.imshow("Cropped Output",imgCropped)
cv2.waitKey(0)