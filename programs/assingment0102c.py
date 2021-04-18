"""This is a test program."""

import cv2
#import numpy as np

img = cv2.imread("fox.jpg", 1)

height = img.shape[0]
width = img.shape[1]

img3 = cv2.resize(img, (int(width/2), int(height/2)))

cv2.imwrite("small_fox.jpg", img3)
cv2.imshow("image3", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
