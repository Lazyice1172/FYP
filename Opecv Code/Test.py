import cv2
import numpy as np

def balance_contrast(image_path):
    # Read the image
    original_image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    # Compute the gradient magnitude using the Sobel operator
    sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=5)
    gradient_magnitude = np.sqrt(sobelx**2 + sobely**2)

    # Normalize the gradient magnitude to the range [0, 255]
    gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)

    # Apply adaptive thresholding to the gradient magnitude to find significant edges
    _, edges = cv2.threshold(gradient_magnitude.astype(np.uint8), 30, 255, cv2.THRESH_BINARY)

    # Find contours in the edges
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through the contours and find the inner rectangle
    max_area = 0
    max_contour = None
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            max_contour = contour

    # Create a mask for the inner rectangle
    mask = np.zeros(gray_image.shape, dtype=np.uint8)
    cv2.drawContours(mask, [max_contour], -1, 255, thickness=cv2.FILLED)

    # Apply histogram equalization to the inner rectangle
    inner_rectangle = cv2.bitwise_and(gray_image, gray_image, mask=mask)
    equalized_inner_rectangle = cv2.equalizeHist(inner_rectangle)

    remove_inner =cv2.subtract(gray_image, inner_rectangle)

    result_image = cv2.bitwise_or(remove_inner, equalized_inner_rectangle)



    # Display the original image with the balanced contrast
    cv2.imshow('Balanced Contrast', result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Specify the path to the image
image_path = 'faded.jpg'

# Balance the contrast and display the result
balance_contrast(image_path)
