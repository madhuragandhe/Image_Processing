from skimage import io
from skimage import transform as td
from matplotlib import pyplot as plt

img=io.imread("cat.jpg")

# ROTATE
# rot=td.rotate(img,45)
# plt.figure(0)
# plt.title("ROTATE")
# io.imshow(rot)

# RESIZE
# res=td.resize(img,(50,50))
# plt.figure(1)
# plt.title("RESIZE")
# io.imshow(res)

# RESCALE
# resc=td.rescale(img,10)
# plt.figure(2)
# plt.title("RESCALE")
# io.imshow(resc)


# RESIZE
# pyr=td.pyramid_expand(img)
# pyr=td.pyramid_reduce(img)
# pyr=td.pyramid_gaussian(img)
# pyr=td.pyramid_laplacian(img)
# plt.figure(3)
# plt.title("PYRAMIDS")
# io.imshow(pyr)

plt.show()