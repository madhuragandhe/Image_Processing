from skimage import io
from skimage import color
from matplotlib import pyplot as plt

# Read image
img=io.imread("cat.jpg")

# Convert to YPbPr
to_ypbpr=color.rgb2ypbpr(img)

# Convert back to RGB
to_rgb=color.ypbpr2rgb(to_ypbpr)

# Save image
# io.imsave("Cat_YPbPr",to_ypbpr)
# plt.save(to_ypbpr,"cat2")
# plt.imsave("cat2",to_ypbpr)
plt.imsave(to_ypbpr,"cat2")
