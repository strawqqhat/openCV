import cv2
import numpy as np
img = cv2.imread('image0.jpg', 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
for m in range(100, 300):
    for n in range(100, 200):
        #pixel -> 10*10
        if m%10 == 0 and n%10==0:
            for i in range(0, 10):
                for j in range(0, 10):
                    (b, g, r) = img[m, n]
                    img[i+m, j+n] = (b, g, r)
cv2.imshow('dst', img)
cv2.waitKey(0)

