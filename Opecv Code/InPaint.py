import cv2
import numpy as np


def restore_damaged(damaged_img):
    handle_img = damaged_img.copy()
    hsv = cv2.cvtColor(handle_img, cv2.COLOR_BGR2HSV)

    sensitivity = 50
    lower_white = np.array([0, 0, 255 - sensitivity])
    upper_white = np.array([255, sensitivity, 255])

    thresh = cv2.inRange(hsv, lower_white, upper_white)

    kernel = np.ones((3, 3), np.uint8)

    dilate_res = cv2.dilate(thresh, kernel, iterations=1)

    dst = cv2.inpaint(handle_img, dilate_res, 3, cv2.INPAINT_TELEA)

    cv2.imshow("output1", handle_img)
    cv2.imshow("output2", thresh)
    cv2.imshow("output3", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    damaged_img = cv2.imread(filename="PJM-814x1024.jpg")
    restore_damaged(damaged_img)
