import cv2
import numpy as np
img = cv2.imread('image0.jpg', 1)
cv2.imshow('src', img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]

matShift = np.float32([[1, 0, -100], [0, 1, 200]])
dst = cv2.warpAffine(img, matShift, (height, width)) # 1 data 2 mat 3 info
cv2.imshow('dst', dst)
cv2.waitKey(0)