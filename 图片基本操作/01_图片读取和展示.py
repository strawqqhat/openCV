import cv2
img = cv2.imread('image0.jpg', 1)
cv2.imwrite('image1.jpg', img)
cv2.imshow('image', img)
cv2.waitKey(0)