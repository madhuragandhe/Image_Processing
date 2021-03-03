import cv2

# In this we look at edge detection using Sobel derivatives.
# We emphasize on those regions that have very high spatial frequency,
# which may correspond to edges.

img=cv2.imread("dog.jpg")

# Apply gaussian blur (to remove noise)
cv2.GaussianBlur(img,(3,3),0)

# Convert image to grayscale
grayImg=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

# Apply Sobel method to grayscale image

# Horizontal Sobel Derivative
grad_x=cv2.Sobel(grayImg,cv2.CV_16S,1,0,ksize=3,scale=1,delta=0,borderType=cv2.BORDER_DEFAULT)

# Vertical Sobel Derivative
grad_y=cv2.Sobel(grayImg,cv2.CV_16S,0,1,ksize=3,scale=1,delta=0,borderType=cv2.BORDER_DEFAULT)

abs_grad_x=cv2.convertScaleAbs(grad_x)
abs_grad_y=cv2.convertScaleAbs(grad_y)
grad=cv2.addWeighted(abs_grad_x,0.5,abs_grad_y,0.5,0)

# Show the image
cv2.imshow(winname='Gradient descent',mat=grad)
cv2.waitKey(0)
cv2.destroyAllWindows()

