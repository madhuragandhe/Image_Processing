from skimage import io
from skimage import color
import matplotlib.pyplot as plt

# RGB to HSV
img=io.imread('cat.jpg')
spaces=['rgb2hsv','rgb2xyz','rgb2grey','rgb2yuv','rgb2lab','rgb2yiq','rgb2ypbpr']

# few more functions to use if want to convert from different color space to RGB
# ['hsv2rgb','xyz2rgb','grey2rgb','yuv2rgb','lab2rgb','yiq2rgb','ypbpr2rgb']


img0_=color.rgb2hsv(img)
img1_=color.rgb2xyz(img)
img2_=color.rgb2grey(img)
img3_=color.rgb2lab(img)
img4_=color.rgb2yiq(img)
img5_=color.rgb2yuv(img)
img6_=color.rgb2ypbpr(img)

plt.figure(0)
plt.title("RGB")
io.imshow(img)

plt.figure(1)
plt.title("HSV")
io.imshow(img0_)

plt.figure(2)
plt.title("XYZ")
io.imshow(img1_)

plt.figure(3)
plt.title("GREY")
io.imshow(img2_)

plt.figure(4)
plt.title("LAB")
io.imshow(img3_)

plt.figure(5)
plt.title("YIQ")
io.imshow(img4_)

plt.figure(6)
plt.title("YUV")
io.imshow(img5_)

plt.figure(7)
plt.title("YPbPr")
io.imshow(img6_)

plt.show()