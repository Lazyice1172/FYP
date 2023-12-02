import numpy as np
import cv2 as cv
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import image as image

# Main()

# 1. Create a blank image

img = np.zeros((512, 512, 3), np.uint8)

print(img.shape)
x, y, z = img.shape
print(img[0, 0, 0])

# 2. Draw on the image

cv.line(img, (0,0), (511, 511), (255, 0, 0), 5)
cv.rectangle(img, (384, 0), (511, 128), (0, 255, 0), 5)
cv.circle(img, (255, 255), 50, (0, 0, 255), -1)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, "OpenCV", (10, 500), font, 1, (255, 255, 255), 3, cv.LINE_AA)

# 3. Display image
cv.imshow("", img)
cv.waitKey(0)
cv.destroyAllWindows()


# End Main()
