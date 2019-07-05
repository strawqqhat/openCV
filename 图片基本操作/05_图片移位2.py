import cv2
import numpy as np
img = cv2.imread('image0.jpg', 1)
cv2.imshow('src', img)
imgInfo = img.shape
dst = np.zeros(img.shape, np.uint8)
height = imgInfo[0]
width = imgInfo[1]
for i in range(0, height):
    for j in range(0, width-100):
        dst[i, j+100] = img[i, j]
cv2.imshow('image', dst)
cv2.waitKey(0)