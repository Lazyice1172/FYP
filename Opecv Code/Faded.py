import cv2
import numpy as np

def restore_faded_image(image_path):
    # Read the image
    original_image = cv2.imread(image_path)

    # Convert the image to LAB color space
    lab_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2LAB)

    # Separate the LAB channels
    l_channel, a_channel, b_channel = cv2.split(lab_image)

    # Apply histogram equalization to the L channel
    equalized_l_channel = cv2.equalizeHist(l_channel)

    # Apply contrast stretching to the L channel
    min_intensity = np.min(equalized_l_channel)
    max_intensity = np.max(equalized_l_channel)
    stretched_l_channel = (255.0 / (max_intensity - min_intensity) * (equalized_l_channel - min_intensity)).astype(np.uint8)

    # Merge the stretched L channel with the original A and B channels
    enhanced_lab_image = cv2.merge([stretched_l_channel, a_channel, b_channel])

    # Convert the image back to BGR color space
    restored_image = cv2.cvtColor(enhanced_lab_image, cv2.COLOR_LAB2BGR)

    # Display the original and restored images side by side
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Restored Image', restored_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the restored image
    cv2.imwrite('restored_image.jpg', restored_image)

# Specify the path to the faded image
image_path = 'faded2.jpg'

# Restore the faded image
restore_faded_image(image_path)
