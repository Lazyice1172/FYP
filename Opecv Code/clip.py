import cv2
import numpy as np
from matplotlib import pyplot as plt


# Please DO NOT add any additional imports to this notebook
# Functionality using libraries other than those listed above will not be graded


def process_image(I: np.ndarray) -> np.ndarray:

    new_image = np.zeros(I.shape, I.dtype)

    alpha = 1.0
    beta = 0

    # Initialize values
    print(' Basic Linear Transforms ')
    print('-------------------------')
    try:
        alpha = float(input('* Enter the alpha value [1.0-3.0]: '))
        beta = int(input('* Enter the beta value [0-100]: '))
    except ValueError:
        print('Error, not a number')

    for y in range(I.shape[0]):
        for x in range(I.shape[1]):
            for c in range(I.shape[2]):
                new_image[y, x, c] = np.clip(alpha * I[y, x, c] + beta, 0, 255)

    return new_image



fig, axs = plt.subplots(2, 2)
original_faded = cv2.imread('faded2.jpg')
improved_faded = process_image(original_faded)

cv2.imshow("Original", original_faded)
cv2.imshow("Improved", improved_faded)
cv2.waitKey(0)
cv2.destroyAllWindows()
