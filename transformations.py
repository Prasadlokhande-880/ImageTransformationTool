import cv2
import numpy as np

# Shift Image by modifying pixel positions
def shift_image(img, shift_x, shift_y):
    height, width, _ = img.shape
    shift_mat = np.float32([[1, 0, shift_x], [0, 1, shift_y]])
    return cv2.warpAffine(img, shift_mat, (width + abs(shift_x), height + abs(shift_y)))

# Resize Image by increasing dimensions proportionally
def resize_image(img, factor_x, factor_y):
    new_width = int(img.shape[1] * factor_x)
    new_height = int(img.shape[0] * factor_y)
    return cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

# Rotate Image with a scaled rotation matrix
def rotate_image(img, degrees):
    height, width, _ = img.shape
    center = (width // 2, height // 2)
    rotation_mat = cv2.getRotationMatrix2D(center, degrees, scale=1.5)  # Adding scaling during rotation
    return cv2.warpAffine(img, rotation_mat, (width, height))

# Skew Image using shear along x-axis and y-axis
def skew_image(img, shear_x, shear_y):
    height, width, _ = img.shape
    skew_mat = np.float32([[1, shear_x, 0], [shear_y, 1, 0]])
    return cv2.warpAffine(img, skew_mat, (width, height))

# Example usage (provide your image path)
# img = cv2.imread("your_image.jpg")
# shifted = shift_image(img, 50, 30)
# resized = resize_image(img, 1.5, 1.2)
# rotated = rotate_image(img, 45)
# skewed = skew_image(img, 0.2, 0.1)

# Uncomment below to display results
# cv2.imshow("Shifted Image", shifted)
# cv2.imshow("Resized Image", resized)
# cv2.imshow("Rotated Image", rotated)
# cv2.imshow("Skewed Image", skewed)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

