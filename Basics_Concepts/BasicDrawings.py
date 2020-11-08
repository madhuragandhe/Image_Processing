from skimage import io
from skimage import draw
import matplotlib.pyplot as plt

img=io.imread("cat.jpg")

# Creating a line
x,y= draw.line(0,0,170,120)
img[x,y]=1

x,y= draw.line(45,40,0,150)
img[x,y]=1

io.imshow(img)
plt.title("--LINE--")
plt.show()

# Creating a polygon
## Rectangle
def rectangle(x,y,w,h):
    rr,cc=[x,x+w,x+w,x],[y,y,y+h,y+h]
    return(draw.polygon(rr,cc))

rr,cc=rectangle(35,100,105,102)
img[rr,cc]=1

io.imshow(img)
plt.title("[]..RECTANGLE..[]")
plt.show()

# Creating a circle
x,y=draw.circle(100,125,10)
img[x,y]=1

x,y=draw.circle(83,170,10)
img[x,y]=1

io.imshow(img)
plt.title("o..CIRCLE..o")
plt.show()

# Creating a Bezier curve
x,y=draw.bezier_curve(87,15,100,25,65,120,100)
img[x,y]=1

io.imshow(img)
plt.title("(..BEZIER CURVE..)")
plt.show()

# Creating a ellipse
x,y=draw.ellipse(10,15,10,15,rotation=50)
img[x,y]=1

io.imshow(img)
plt.title("0..ELLIPSE..0")
plt.show()