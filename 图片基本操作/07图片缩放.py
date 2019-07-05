import cv2
import numpy as np
img = cv2.imread('image0.jpg', 1)
cv2.imshow('src', img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
matScale = np.float32([[0.5, 0, 0], [0, 0.5, 0]])
dst = cv2.warpAffine(img, matScale, (int(width/2), int(height/2)))
cv2.imshow('dst', dst)
cv2.waitKey(0)