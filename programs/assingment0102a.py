"""This is a test program."""

import cv2
#import numpy as np

img = cv2.imread("fox.jpg", 1)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
