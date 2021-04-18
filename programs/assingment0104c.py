"""This is a test program."""
import cv2

img = cv2.imread("fox.jpg")

detector = cv2.ORB_create()

kp = detector.detect(img)

out = cv2.drawKeypoints(img, kp, None)

cv2.imwrite("ORB_fox.jpg", out)
cv2.imshow("orb", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
