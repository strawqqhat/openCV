import cv2
import numpy as np
img = cv2.imread('image0.jpg', 1)
cv2.imshow('src', img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
matSrc = np.float32([[0, 0], [0, height-1], [width-1, 0]])
matDst = np.float32([[50, 50], [300, height-200], [width-300, 100]])
matAffine = cv2.getAffineTransform(matSrc, matDst)
dst = cv2.warpAffine(img, matAffine, (width, height))
cv2.imshow('dst', dst)
cv2.waitKey(0)