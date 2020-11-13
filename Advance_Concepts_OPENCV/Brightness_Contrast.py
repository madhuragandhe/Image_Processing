import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import io

# Read image
img1=cv2.imread("dog.jpg")

# Create a dummy image that stores Contrast and Brightness
dummy_img=np.zeros(img1.shape,img1.dtype)

# Brightness and Contrast parameters
brightness=3
contrast=2

# Change the contrast and brightness
    # First for loop gives image width
    # Second for loop gives image height
    # Third for loop gives image channels(eg:if RGB it runs 3 times)
for w in range(img1.shape[0]):
    for h in range(img1.shape[1]):
        for c in range(img1.shape[2]):
            # np.clip(array,array.min,array.max)
            # Formula used = (Specific pixel value * Contrast) + Brightness
            dummy_img[w,h,c]=np.clip(img1[w,h,c]*contrast+brightness,0,255)

plt.figure(0)
plt.title("Original image")
io.imshow(img1)
plt.figure(1)
plt.title("Bright-Contrast image")
io.imshow(dummy_img)

plt.show()













