import cv2
import numpy as np

img1 = np.zeros((720,1277, 3), np.uint8)
img1 = cv2.rectangle(img1, (600, 0), (1000,100), (255,255,255), -1)
img2 = cv2.imread("image_1.png")

bitAnd = cv2.bitwise_and(img2, img2)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("bitAnd", bitAnd)
cv2.waitKey()
cv2.destroyAllWindows()