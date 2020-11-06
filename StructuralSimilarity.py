from skimage import io
from matplotlib import pyplot as plt
from skimage.measure import compare_ssim as ssim

img1=io.imread("cat.jpg")
img2=io.imread("Photo.jpg")

ssim_img1=ssim(img1,img1,data_range=img1.max()-img1.min(),multichannel=True)
ssim_img2=ssim(img1,img2,data_range=img2.max()-img2.min(),multichannel=False)

print(ssim_img1," - ",ssim_img2)