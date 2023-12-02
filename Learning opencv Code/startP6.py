

# Class follow by
# https://www.bilibili.com/video/BV1kv4y1J784?p=1&vd_source=93b2c47157c4d48a50b5265000bb4fba


import cv2 as cv
import numpy as np

import matplotlib
from matplotlib import pyplot as plt
from matplotlib import image as image

# 1 => color
# 0 => gray
# -1 => alpah channel
img = cv.imread("Image_Resource/Googly.jpg", 1)
print(img[30, 30, :])


# opencv always read image with BGR channel rather is RGB


# show image with openCV
cv.imshow("", img)
cv.waitKey(0)
cv.destroyAllWindows()

# show image with pyplot
# plt.imshow(img)
# plt.show()

# store image
cv.imwrite("image name.jpg", img)