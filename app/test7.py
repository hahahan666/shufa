import cv2
import numpy as np

# Load image
img = cv2.imread('./image.jpg', cv2.IMREAD_UNCHANGED)

# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

# Define range of red color in HSV
lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])
mask_red = cv2.inRange(hsv, lower_red, upper_red)

# Define range of black color in HSV
lower_black = np.array([0,0,0])
upper_black = np.array([180,255,30])
mask_black = cv2.inRange(hsv, lower_black, upper_black)

# Define range of white color in HSV
lower_white = np.array([0,0,231])
upper_white = np.array([180,30,255])
mask_white = cv2.inRange(hsv, lower_white, upper_white)

# Bitwise-AND mask and original image
res_red = cv2.bitwise_and(img,img, mask= mask_red)
res_black = cv2.bitwise_and(img,img, mask= mask_black)
res_white = cv2.bitwise_and(img,img, mask= mask_white)

# Display images
cv2.imshow('Original',img)
cv2.imshow('Red',res_red)
cv2.imshow('Black',res_black)
cv2.imshow('White',res_white)
cv2.waitKey(0)
cv2.destroyAllWindows()