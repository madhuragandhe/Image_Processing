
  **1. Blending two images** <br>
       Two images are blend in such a way that features of both images are visible.<br>
       We use image registration techniques to blend one image over the second one <br>
       and determine whether there are any changes.<br>
       Some of the functions used in the code:<br>
       <ol>
           - *cv2.imread()*: This function is used to read the image from a particular destination. <br>
           - *cv2.addWeighted()*: This function blends the two images.The arguments are *(image1,alpha,image2,beta,gamma)*.The alpha and beta parameters indicate the transparency                                   in both images.The last parameter is called gamma.It is just a scalar, which is added to the formulas,to transform the images more effectively.<br>
           - *cv2.imshow()*: It helps to display the image in a new window.<br>
           - *cv2.waitKey()*: This function is used so that the window displaying the output remains until we click Close or press Escape, zero as an argument says thst the window is displayed for an infinite time.<br>
           - *cv2.DestroyAllWindows()*: After we have clicked Close or pressed the Escape, this function destroys all the windows that ahve been opened and saved in the memory. <br>
       </ol>
       [code](https://github.com/madhuragandhe/Image_Processing/blob/master/Advance_Concepts_OPENCV/BlendingImgs.py)<br>
       
   **2. Chnaging Contrast and Brightness** <br>
       *Contrast*: It is the difference between maximum and minimum pixel intensity.<br>
       *Brightness*: It refers to the lightness or darkness of an image. To make an image brighter, we add a constant number to all pixels present in it. <br>
    
       [code]()<br>


