"""This is a test program."""

import cv2
#import numpy as np
#from matplotlib import pylab as plt

img0 = cv2.imread("diff0.png", 0)
img1 = cv2.imread("diff1.png", 0)

img_diff = cv2.absdiff(img0, img1)

ret, img_bin = cv2.threshold(img_diff, 50, 255, 0)

cv2.imwrite("difference.jpg", img_bin)
cv2.imshow("frame", img_bin)
cv2.waitKey(0)
cv2.destroyAllWindows()
