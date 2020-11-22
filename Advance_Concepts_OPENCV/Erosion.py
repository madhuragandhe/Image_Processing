from matplotlib import pyplot as plt
from skimage import io
import cv2

# Changing the shape of the image
# two types 1) Erosion 2) Dilation

# EROSION : Removal of pixels from the boundary of the object

image=cv2.imread("cat.jpg")

# Define erosion size
e1=0
e2=10
e3=20

# Define erosion type
t1=cv2.MORPH_RECT
t2=cv2.MORPH_CROSS
t3=cv2.MORPH_ELLIPSE

# Define and save the erosion template
temp1=cv2.getStructuringElement(t1,(2*e1+1,2*e1+1),(e1,e1))
temp2=cv2.getStructuringElement(t2,(2*e2+1,2*e2+1),(e2,e2))
temp3=cv2.getStructuringElement(t3,(2*e3+1,2*e3+1),(e3,e3))

# Apply th erosion template to the image and save it
final1=cv2.erode(image,temp1)
final2=cv2.erode(image,temp2)
final3=cv2.erode(image,temp3)

plt.figure(0)
plt.title("MORPH_RECT")
io.imshow(final1)

plt.figure(1)
plt.title("MORPH_CROSS")
io.imshow(final2)

plt.figure(2)
plt.title("MORPH_ELLIPSE")
io.imshow(final3)

plt.show()