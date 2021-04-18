"""This is a test program."""

import cv2
#import numpy as np

img = cv2.imread("fox.jpg", 1)

threshold = 100

ret, img5 = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

cv2.imwrite("threshold_fox.jpg", img5)
cv2.imshow("image5", img5)
cv2.waitKey(0)
cv2.destroyAllWindows()
