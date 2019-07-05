import cv2
import numpy as np
import math
img = cv2.imread('image0.jpg',1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
cv2.imshow('src', img)
# sobel 1 算子模板 2 图片卷积 3 阈值判决
# [1 2 3 4] [a b c d] a*1+b*2+c*3+d*4 = dst
# sqrt(a*a+b*b) = f>th
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst = np.zeros((height, width, 1), np.uint8)
for i in range(0, height-2):
    for j in range(0, width-2):
        gy = gray[i,j]*1+gray[i,j+1]*2+gray[i,j+2]*1-gray[i+2,j]*1-gray[i+2,j+1]*2-gray[i+2,j+2]*1
        gx = gray[i,j]*1+gray[i+1,j]*2+gray[i+2,j]*1-gray[i,j+2]*1-gray[i+1,j+2]*2-gray[i+2,j+2]*1
        grad = math.sqrt(gx*gx+gy*gy)
        if grad > 50:
            dst[i, j] = 255
        else:
            dst[i, j] = 0
cv2.imshow('dst', dst)
cv2.waitKey(0)