import cv2
from matplotlib import pyplot as plt
from skimage import io

# 3 filters to smooth images
# Median filter
# Gaussian filter
# Bilateral filter

img=cv2.imread("cat.jpg")
img_medianBlur=cv2.imread("cat.jpg")
img_gaussianBlur=cv2.imread("cat.jpg")
img_bilateralBlur=cv2.imread("cat.jpg")

# Blur images
img_medianBlur=cv2.medianBlur(img_medianBlur,9)
img_gaussianBlur=cv2.GaussianBlur(img_gaussianBlur,(9,9),10)
img_bilateralBlur=cv2.bilateralFilter(img_bilateralBlur,25,200,64)

plt.figure(0)
plt.title("Normal")
io.imshow(img)
#
# plt.figure(1)
# plt.title("MEDIAN BLUR")
# io.imshow(img_medianBlur)
#
# plt.figure(2)
# plt.title("GAUSSIAN BLUR")
# io.imshow(img_gaussianBlur)

plt.figure(3)
plt.title("BILATERAL BLUR")
io.imshow(img_bilateralBlur)

plt.show()