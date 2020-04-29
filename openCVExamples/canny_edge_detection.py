import cv2
import numpy as np
from matplotlib import pyplot as plt

def trackChaned(x):
    pass


cv2.namedWindow('Color Track Bar')
hh = 'Max'
hl = 'Min'
wnd = 'Colorbars'
cv2.createTrackbar("Max", "Color Track Bar", 0, 300, trackChaned)
cv2.createTrackbar("Min", "Color Track Bar", 0, 300, trackChaned)


while(1):
  img = cv2.imread("messi5.jpg", 0)
  hul = cv2.getTrackbarPos("Max", "Color Track Bar")
  huh = cv2.getTrackbarPos("Min", "Color Track Bar")
  canny = cv2.Canny(img, 100, 200)


cv2.imshow('canny',canny)


cv2.waitKey(0)
cv2.destroyAllWindows()



