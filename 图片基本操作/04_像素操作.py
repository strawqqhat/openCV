import cv2
img = cv2.imread('image0.jpg', 1)
(b, g, r) = img[200][200]
print(b, g, r)

for i in range(1,200):
    img[10+i][100] = (255, 0, 0)

cv2.imshow('image', img)
cv2.waitKey(0)