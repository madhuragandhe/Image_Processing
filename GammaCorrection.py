from skimage import io
from skimage import exposure
from matplotlib import pyplot as plt

img=io.imread('cat.jpg')
plt.figure(0)
plt.title("Original")
io.imshow(img)

gamma_correct=exposure.adjust_gamma(img,0.5)
plt.figure(1)
plt.title("Gamma 0.5")
io.imshow(gamma_correct)


gamma_correct1=exposure.adjust_gamma(img,5)
plt.figure(2)
plt.title("Gamma 5")
io.imshow(gamma_correct1)
plt.show()
