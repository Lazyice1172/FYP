import numpy as np
import cv2 as cv
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import image as image

# Main()

# Img algorithm
# Both Image must have the same size

x = np.uint8([250])
y = np.uint8([10])

print(cv.add(x, y)) # 250 + 10 = 260 => 255

print(x + y) # 250 + 10 = 260 % 256 = 4


# Example

img1 = cv.imread("Image_Resource/water.jpg")
img2 = cv.imread("Image_Resource/orange.png")

print(img1.shape)
print(img2.shape)

img3 = cv.add(img1, img2)
img4 = img1+img2

cv.imshow("img3", img3)
cv.imshow("img4", img4)

cv.waitKey(0)
cv.destroyAllWindows()

# Example 2

img5 = cv.subtract(img1, img2)
img6 = img1-img2

cv.imshow("img5", img5)
cv.imshow("img6", img6)

cv.waitKey(0)
cv.destroyAllWindows()

# Example 3


img7 = cv.multiply(img1, img2, scale=0.1)
img8 = img1 * img2

cv.imshow("img7", img7)
cv.imshow("img8", img8)

cv.waitKey(0)
cv.destroyAllWindows()

# Example 4

img9 = cv.divide(img1, img2 , scale=100)
img10 = img1 / img2 # with have Zero wranning

cv.imshow("img9", img9)
cv.imshow("img10", img10)

cv.waitKey(0)
cv.destroyAllWindows()

# End Main()
