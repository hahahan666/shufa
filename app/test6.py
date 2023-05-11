import cv2
import numpy as np

# Load image
img = cv2.imread('image.jpg')

# Resize image
scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

# Convert to HSV color space
hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)

# Define range of red color in HSV
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])
mask1 = cv2.inRange(hsv, lower_red, upper_red)

lower_red = np.array([170, 50, 50])
upper_red = np.array([180, 255, 255])
mask2 = cv2.inRange(hsv, lower_red, upper_red)

# Combine the masks
mask = mask1 + mask2

# Apply the mask to the image
result = cv2.bitwise_and(resized, resized, mask=mask)

# Display the result
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()