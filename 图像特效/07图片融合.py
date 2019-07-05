import cv2
import numpy as np
img0 = cv2.imread('image0.jpg',1)
img1 = cv2.imread('image1.jpg',1)
imgInfo = img0.shape
height = imgInfo[0]
width = imgInfo[1]

roiH = int(height/2)
roiW = int(width/2)
img0ROI = img0[0:roiH, 0:roiW]
img1ROI = img1[0:roiH, 0:roiW]
dst = np.zeros((roiH, roiW, 3), np.uint8)
dst = cv2.addWeighted(img0ROI, 0.5, img1ROI, 0.5, 0)
# add src1*a+src2*(1-a)
cv2.imshow('dst', dst)
cv2.waitKey(0)