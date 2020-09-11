from skimage import io
import matplotlib.pyplot as plt


image=io.imread('cat.jpg')
plt.imshow(image)
plt.show()