"""This is a test program."""

import cv2
#import numpy as np

img = cv2.imread("fox.jpg", 1)

img4 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite("rotate_fox.jpg", img4)
cv2.imshow("image4", img4)
cv2.waitKey(0)
cv2.destroyAllWindows()
