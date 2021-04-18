"""This is a test program."""
import cv2
#import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("fox.jpg", 0)

plt.hist(img.ravel(), 256, [0, 256])
plt.savefig('hist_fox.jpg')
plt.show()
