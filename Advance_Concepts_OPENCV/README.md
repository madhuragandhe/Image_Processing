
  **1. Blending two images** <br>
       Two images are blend in such a way that features of both images are visible.<br>
       We use image registration techniques to blend one image over the second one <br>
       and determine whether there are any changes.<br>
       Some of the functions used in the code:<br>
       <ol>
           - *cv2.imread()*: This function is used to read the image from a particular destination. <br>
           - *cv2.addWeighted()*: This function blends the two images.The arguments are *(image1,alpha,image2,beta,gamma)*.The alpha and beta parameters indicate the transparency                                   in both images.The last parameter is called gamma.It is just a scalar, which is added to the formulas,to transform the images more effectively.<br>
           - *cv2.imshow()*: <br>
           - *cv2.waitKey()*: <br>
           - *cv2.DestroyAllWindows()*: <br>
       </ol>
       [code]()<br>

