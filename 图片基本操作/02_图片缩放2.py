import cv2
import numpy as np
img = cv2.imread('image0.jpg', 1)
imgInfo = img.shape
print(imgInfo)
height = imgInfo[0]
width = imgInfo[1]
mode = imgInfo[2]

dstHeight = int(height*0.5)
dstWidth = int(width*0.5)

dstImage = np.zeros((dstHeight, dstWidth, 3), np.uint8)
for i in range(0, dstHeight):
    for j in range(0, dstWidth):
        iNew = int(i*(height*1.0/dstHeight))
        jNew = int(j*(width*1.0/dstWidth))
        dstImage[i][j] = img[iNew][jNew]
cv2.imshow('image', dstImage)
cv2.waitKey(0)
