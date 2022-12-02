import cv2
import numpy as np

INPUT_IMAGE = "./images/Lena-original-gray.png"
SEPARATE_WINDOWS = False
LEVEL_VECTOR = np.array([0, 63, 127, 191, 255], dtype=np.int16)

img = cv2.imread(INPUT_IMAGE, cv2.IMREAD_GRAYSCALE)

def proximateGrayLevelAndDifference(grey_color):
    levels = np.copy(LEVEL_VECTOR)
    levels = np.abs(levels - grey_color)
    diff = np.min(levels)
    diff_index = np.where(levels == diff)[0][0]
    selected_grey_color = LEVEL_VECTOR[diff_index]

    # returning the difference between the pixesl, without absolute path
    return selected_grey_color, (grey_color - selected_grey_color)

def errorDiffusion(img):
    output_image = np.copy(img)

    rows, cols = output_image.shape

    for i in range(0, rows):
        for j in range(0, cols):
            grey_color = output_image[i, j]
            new_color, diff = proximateGrayLevelAndDifference(grey_color)
            output_image[i, j] = new_color

            # If the pixel is not on the right or bottom edges
            if i < rows - 1 and j < cols - 1:
                output_image[i, j+1] += int(3 * diff / 8)
                output_image[i + 1, j] += int(3 * diff / 8)
                output_image[i + 1, j + 1] += int(diff / 4)
    
    return output_image

output_image = errorDiffusion(img)

if not SEPARATE_WINDOWS:
    result = np.concatenate([img, output_image], axis=1)
    cv2.imshow("Left to Right: Before and After Error Diffusion", result)
else:
    cv2.imshow('before error diffusion', img)
    cv2.imshow('after error diffusion', output_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('./output/after-error-diffusion.png', output_image)
