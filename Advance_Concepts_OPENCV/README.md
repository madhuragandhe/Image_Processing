
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
       *cv2.putText()* is a function present in cv2 module that allows us to add text.<br>
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
           - FONT_HERSHEY_SIMPLEX<br>
           - FONT_HERSHEY_PLAIN<br>
           - FONT_HERSHEY_DUPLEX<br>
           - FONT_HERSHEY_COMPLEX<br>
           - FONT_HERSHEY_TRIPLEX<br>
           - FONT_HERSHEY_COMPLEX_SMALL<br>
           - FONT_HERSHEY_SCRIPT_SIMPLEX<br>
           - FONT_HERSHEY_SCRIPT_COMPLEX<br>
           - FONT_ITALIC<br>
       </ol>
       <br>
       Types of LINES used are:
       <ol>
           - FILLED: a completely filled line<br>
           - LINE_4: four connected lines<br>
           - LINE_8: eight connected lines<br>
           - LINE_AA: an anti-aliasing lines<br>
       </ol>
       <br>
       [code](https://github.com/madhuragandhe/Image_Processing/blob/master/Advance_Concepts_OPENCV/Text_on_Image.py)
       <br>
       **4. Smoothing Images** <br>
          *A) Median Filter* <br>
          <ol>
              - It is a non linear filter that removes black and white noise present in an image by finding the median using the neighboring filters.<br>
              - To smooth an image, we look at the first 3x3 matrix, find the median of that matrix,replace the central value by that median.<br>
              - Next,move one step to the right and repeat the process until all pixels have been covered.<br>
              - The final image is the smoothed image.<br>
              - Median Filter is the best option when you want to preserve the edges of your image while blurring.<br>
          </ol>
          *cv2.medianBlur*, is the function used to achieve median blur.<br>
          It has two parameters:<br>
          <ol>
              1. The image we want to smooth.<br>
              2. The kernel size, which should be odd.Thus a value of 9 means a 9x9 matrix.
          </ol>
       <br>
       *B) Gaussian Filter* <br>
          <ol>
              - It depends on the standard deviation of the image and assumes the mean as zero.<br>
              - Gaussian filter do not take care of the edges.<br>
              - It is used for basic image blurring.<br>
              - We define a kernel.<br>
              - Then we apply this kernel to each and every pixel present in the image, and average the result, which results in a blurred image.<br>
          </ol>
          *cv2.GaussianBlur*, is the function used to apply gaussian filter.<br>
          It has three parameters:<br>
          <ol>
              1. The image to be blurred.<br>
              2. The kernel size.<br>
              3. The standard deviation<br>
          </ol>
       <br>
        *B) Bilateral Filter* <br>
          <ol>
              - It is used where we have to smooth an image and keep the edges intact.<br>
              - We replace the pixel value with the average of its neighbors.<br>
              - Neighbors are defined in the following ways:<br>
              <ol>
                  - Two pixel values are close to each other (using sapce)<br>
                  - Two pilex values are similar to each other (using color)<br>
              </ol>
          </ol>
          *cv2.bilateralFilter*, is the function used to apply gaussian filter.<br>
          It has three parameters:<br>
          <ol>
              1. The image we want to smooth<br>
              2. The diameter of the pixel neighborhood (neighborhood diameter to search for neighbors)<br>
              3. The sigma value for color (to find pixels that are similar)<br>
              4. The sigma vlaue for space (to find pixel that are closer)<br>
          </ol>
       <br>
       [code](https://github.com/madhuragandhe/Image_Processing/blob/master/Advance_Concepts_OPENCV/SmoothingImages.py)
       <br>
       **5. Chnaging the Shape of Images ** <br>
       There are two operations (Dilation and Erosion) used to change the shape of the images.<br>
       Dilation results in the addition of pixels to the boundary of an object.<br>
       Erosion leads to the removal of pixels from the boundary.<br>
       To erode or dilate an image, wefirst define the neighborhood kernel, using these three ways:
       <ol>
           - MORPH_RECT: to make rectangular kernel<br>
           - MORPH_CROSS: to make a cross-shaped kernel<br>
           - MORPH_ELLIPS: to make an elliptical kernel<br>
       </ol>
       The kernel finds the neighbors of a pixel, which helps in eroding or dilating an image.<br>
       For Dilation, the maximum value generates a new pixel value.<br>
       For Erosion, the minimum value generates a new pixel value.<br>
       
       [code DILATION](https://github.com/madhuragandhe/Image_Processing/blob/master/Advance_Concepts_OPENCV/Dilation.py)
       [code EROSION](https://github.com/madhuragandhe/Image_Processing/blob/master/Advance_Concepts_OPENCV/Erosion.py)

