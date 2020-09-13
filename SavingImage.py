from skimage import io
from skimage import color

# Read image
img=io.imread("cat.jpg")

# Convert to YPbPr
to_ypbpr=color.rgb2ypbpr(img)

# Convert back to RGB
to_rgb=color.ypbpr2rgb(to_ypbpr)

# Save image
io.imsave("Cat_YPbPr",to_ypbpr)
