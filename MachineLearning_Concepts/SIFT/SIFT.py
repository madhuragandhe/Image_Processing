import cv2
from sift_operations import *

# Read the images
    # make sure that they both are in same folder
x="img1.jpg"
y="img2.jpg"
# x=input("Enter 1st image name")
Img1=cv2.imread(x)
# y=input("Enter 2nd image name")
Img2=cv2.imread(y)

# Convert to grayscale
Img1_gray=cv2.cvtColor(Img1,cv2.COLOR_BGR2GRAY)
Img2_gray=cv2.cvtColor(Img2,cv2.COLOR_BGR2GRAY)

# Extract keypoints and descriptors
Img1_keypoints,Img1_descriptors=extract_sift_features(Img1_gray)
Img2_keypoints,Img2_descriptors=extract_sift_features(Img2_gray)

# Display the sift features
print("Displaying SIFT features")
showing_sift_features(Img1_gray,Img1,Img1_keypoints)

# Find distance between keypoints
norm=cv2.NORM_L2
bruteForce=cv2.BFMatcher(norm)

# Find mathches between the 2 images and sort them
matches=bruteForce.match(Img1_descriptors,Img2_descriptors)
matches=sorted(matches,key=lambda match:match.distance)

# Connect the keypoints
matched_img=cv2.drawMatches(Img1,Img1_keypoints,
                            Img2,Img2_keypoints,
                            matches[:50],Img2.copy())

# plt.figure(figsize=(100,300))
cv2.resizeWindow(winname="sift",width=100,height=300)
cv2.imshow(winname="sift",mat=matched_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


