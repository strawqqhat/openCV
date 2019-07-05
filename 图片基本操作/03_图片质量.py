# import cv2
# img = cv2.imread('image0.jpg', 1)
# cv2.imwrite('imageTest.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50])
#

import cv2
img = cv2.imread('image0.jpg', 1)
cv2.imwrite('imageTest.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
# jpg 0 压缩比高0-100 png 0 压缩比低 0-9
