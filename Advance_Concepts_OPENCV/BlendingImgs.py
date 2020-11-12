import cv2

img1=cv2.imread("cat.jpg")
img2=cv2.imread("dog.jpg")

# Resizing
shape1=img1.shape
shape2=img2.shape
if shape1 != shape2:
    if shape1 > shape2:
        img2=cv2.resize(img2,(img1.shape[1],img1.shape[0]))
    else:
        img1=cv2.resize(img1,(img2.shape[1],img2.shape[0]))

# Define alpha and beta
alpha=0.50
beta=0.50
gamma=60

# Blend images
final_image=cv2.addWeighted(img1,alpha,img2,beta,gamma)

# Show image
cv2.imshow("Blendeds",final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
