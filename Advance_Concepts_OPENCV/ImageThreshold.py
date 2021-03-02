import cv2
from matplotlib import pyplot as plt
from skimage import io

# Read the image
img=cv2.imread("dog.jpg")
# Convert the image to GRAY scale
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

'''
Types of Threshold
----------------------
0-BINARY
1-BINARY INVERTED
2-TRUNCATED
3-THRESHOLD TO ZERO
4-THRESHOLD TO ZERO INVERTED 
'''


_,img1=cv2.threshold(img,50,255,0)
_,img2=cv2.threshold(img,50,255,1)
_,img3=cv2.threshold(img,50,255,2)
_,img4=cv2.threshold(img,50,255,3)
_,img5=cv2.threshold(img,50,255,4)

# Plot the figures
plt.figure(0)
plt.title("Original")
io.imshow(img)

plt.figure(1)
plt.title("Binary")
io.imshow(img1)

plt.figure(2)
plt.title("Binary inv")
io.imshow(img2)

plt.figure(3)
plt.title("Truncated")
io.imshow(img3)

plt.figure(4)
plt.title("Threshold to zero")
io.imshow(img4)

plt.figure(5)
plt.title("Threshold to zero inv")
io.imshow(img5)

plt.show()

if cv2.waitKey(0):
    cv2.destroyAllWindows()
    