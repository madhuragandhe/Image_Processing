
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
       
   **2. Changing Contrast and Brightness** <br>
       *Contrast*: It is the difference between maximum and minimum pixel intensity.<br>
       *Brightness*: It refers to the lightness or darkness of an image. To make an image brighter, we add a constant number to all pixels present in it. <br>
        <br>
        In this code we didnot use any cv2 functions to change brightness or contrast.We use the numpy library and slicing concept to change the parameter.<br>
        *np.clip()* limits the values in a particular range.The formula used is:<br>
        ***(Specific pixel value x Contrast) + Brightness***<br>
        <br>
       [code](https://github.com/madhuragandhe/Image_Processing/blob/master/Advance_Concepts_OPENCV/Brightness_Contrast.py)<br>
   
   **3. Adding Text to Images** <br>
       *cv2,putText()* is a function present in cv2 module that allows us to add text.<br>
       It takes the following arguments:<br>
       <ol>
           - Image, where you want to write the text<br>
           - The text you want to write<br>
           - Position of the text on the image<br>
           - Font type<br>
           - Font scale<br>
           - Color of the text<br>
           - Thickness of the text<br>
           - Type of the line used<br>
       </ol>
       <br>
       Types of FONTS used are:
       <ol>
           - <br>
           - <br>
           - <br>
           - <br>
           - <br>
           - <br>
           - <br>
           - <br>
           - <br>
       </ol>
       <br>
       Types of LINES used are:
       <ol>
           - <br>
           - <br>
           - <br>
           - <br>
           - <br>
           - <br>
           - <br>
           - <br>
           - <br>
       </ol>
       <br>
       [code](https://github.com/madhuragandhe/Image_Processing/blob/master/Advance_Concepts_OPENCV/Text_on_Image.py)<br>


