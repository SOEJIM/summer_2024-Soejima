import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
kerrnel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(img, 100, 100)
imgDialation = cv2.dilate(imgCanny,kerrnel, iterations=1)
imgEroded = cv2.erode(imgDialation,kerrnel, iterations=1)

cv2.imshow("Gray Lena",imgGray)
cv2.imshow("Blur Lena",imgBlur)
cv2.imshow("Canny Lena",imgCanny)
cv2.imshow("Dialation Lena",imgDialation)
cv2.imshow("Eroded Lena",imgEroded)
cv2.waitKey(0)