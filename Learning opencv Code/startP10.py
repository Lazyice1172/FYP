import numpy as np
import cv2 as cv
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import image as image

# Main()

# Change
# img = np.zeros((512, 512, 3), np.uint8
img = cv.imread("Image_Resource/orange.png")

img[100:200, 100:200] = (0, 0, 255)

cv.imshow(" ", img)
cv.waitKey(0)
cv.destroyAllWindows()

# Define
print(img.shape) # shape
print(img.size) # size
print(img.dtype) # type

# Channel split and combine

b, g, r = cv.split(img)

cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red", r)
cv.waitKey(0)
cv.destroyAllWindows()

img = cv.merge((b, g, r))

# Covert color

# Two common
# BGR -> Gray

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray ", gray)

# BGR -> HSV

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

cv.waitKey(0)
cv.destroyAllWindows()


# End Main
