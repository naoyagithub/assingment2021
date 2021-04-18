"""This is a test program."""
import cv2
#import numpy as np

img = cv2.imread("fox.jpg", 0)

sift = cv2.SIFT_create()
kp = sift.detect(img)
img_kp = cv2.drawKeypoints(
    img, kp, img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imwrite("SIFT_fox.jpg", img_kp)
cv2.imshow("img_kp", img_kp)
cv2.waitKey(0)
cv2.destroyAllWindows()
