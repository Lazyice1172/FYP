import cv2
import numpy as np
from matplotlib import pyplot as plt



def process_image(I: np.ndarray) -> np.ndarray:

    copy_img = I.copy()

    hight, width, deep = copy_img.shape
    # print(copy_img.shape)

    lowerRange = np.array([180, 180, 180])
    upperRange = np.array([255, 255, 255])

    thresh_img = cv2.inRange(copy_img, lowerRange, upperRange)
    cv2.imshow("thresh", thresh_img)

    kernal = np.ones((3, 3), np.uint8)

    # iteration is dilate the image how many times
    dilate_res = cv2.dilate(thresh_img, kernal, iterations=1)

    result_img = cv2.inpaint(copy_img, dilate_res, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

    return result_img


# Please DO NOT change any of the code below. All modifications to this template should
# occur inside the **process_image** function

fig, axs = plt.subplots(2, 2)
original_faded = cv2.imread('PJM-814x1024.jpg')
improved_faded = process_image(original_faded)



cv2.imshow("original_faded", original_faded)
cv2.imshow("improved_faded", improved_faded)
cv2.waitKey(0)
cv2.destroyAllWindows()
