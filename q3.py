import cv2
import numpy as np

INPUT_IMAGE = "./images/allColors.png"
SEPARATE_WINDOWS = False

img = cv2.imread(INPUT_IMAGE, cv2.IMREAD_COLOR)

# The default format of cv2 is BGR
# b_color = img[:, :, 0]
# g_color = img[:, :, 1]
# r_color = img[:, :, 2]


hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hue = hsv_img[:, :, 0] # range is 0 - 179
saturation = hsv_img[:, :, 1] # range is 0 - 255
value = hsv_img[:, :, 2] # ragne is 0 - 255

# normalize to values between 0 and 1
norm_hue = hue / 179
norm_saturation = saturation / 255
norm_value = value / 255

if not SEPARATE_WINDOWS:
    result = np.concatenate([norm_hue, norm_saturation, norm_value], axis=1)
    cv2.imshow("Left to Right: Hue Saturation Value", result)
else:
    cv2.imshow('hue image', norm_hue)
    cv2.imshow('saturation image', norm_saturation)
    cv2.imshow('value image', norm_value)

cv2.waitKey(0)
cv2.destroyAllWindows()

# In order to write the images correctly, we need to use the regular ranges of each field
cv2.imwrite('./output/hue.png', hue)
cv2.imwrite('./output/saturation.png', saturation)
cv2.imwrite('./output/value.png', value)
