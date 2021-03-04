import cv2
from matplotlib import pyplot as plt

# Read the image
img=cv2.imread("cat.jpg")

# to apply the histogram equalizaion the image should be in grayscale
# so we
# Convert the image to grayscale
img_G=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

# Apply equalize histogram
img_eqlzd=cv2.equalizeHist(img_G)

cv2.imshow(winname="Equalizer histogram",mat=img_eqlzd)
cv2.imshow(winname="Original",mat=img)
cv2.waitKey(0)
cv2.destroyAllWindows() 