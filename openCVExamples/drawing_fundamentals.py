import numpy as  np
import cv2



#img = cv2.imread('lena.jpg', 1)
img = np.zeros([512,512,3], np.uint8)




img = cv2.rectangle(img, (384,0), (510,128), (125, 0, 215), 10)
img = cv2.circle(img, (447,63), 63, (0,255,0), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', (10,500), font,  4, (255,255,255), 10, cv2.LINE_AA)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()