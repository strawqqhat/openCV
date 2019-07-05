import cv2
import numpy as np
img = cv2.imread('image0.jpg', 1)
cv2.imshow('src', img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
# 2*3
matRotate = cv2.getRotationMatrix2D((height*0.5, width*0.5), 45, 0.5) # mat rotate 1 center 2 angle 3 xishu
dst = cv2.warpAffine(img, matRotate, (height, width))
cv2.imshow('dst', dst)
cv2.waitKey(0)

