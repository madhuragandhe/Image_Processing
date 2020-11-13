import cv2
from skimage import io
from matplotlib import pyplot as plt

# Read image
img=cv2.imread("cat.jpg")
text='I am not a SMELLY cat'
font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
line=cv2.FILLED

# cv2.putText(image,text,position,fontType,fontScale,colorOfText,thicknessOfText,LineType)

cv2.putText(img,text,org=(10,30),fontFace=font,fontScale=0.7,color=(255,23,87),thickness=1,lineType=line)

io.imshow(img)
plt.title("Text on Image")
plt.show()