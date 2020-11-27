
  **1. Uploading and Viewing an Image** <br>
       We start by importing a module named *skimage* .To upload and view an image <br>
       we use the *io* class from the *skimage* module.We use the two function from <br>
       this class:<br>
       <ol>
           - *imread*: to read the image<br>
           - *imshow*: to show the image<br>
       [code](https://github.com/madhuragandhe/Image_Processing/blob/master/Basics_Concepts/Open_Close.py)<br>
       </ol>

  **2. Getting Image Resolution and Pixel Values** <br>
        1. To find the Image Resolution..<br>
        <ol>
            - We use the built in function called *shape*. <br>
            - When an image is read, all the pixel values are stored in an array format; this array is called the *numpy array* .<br>
            - After converting the image to array, we use the *shape* function to look at the resolution.<br>
        </ol>
        2. Looking at the Pixel Values..<br>
        <ol>
           - To read each pixel value we convert the array in dataframe format. <br>
           - We use the function *flatten* to convert the three dimensions of an RGB image to a single dimension.<br> 
           - We then save the image in an excel file named *pixel_values.xlsx*.<br>
           - For this we use a pandas function to_excel.<br>
           - This function converts 1-D array into excel like format, with rows and columns.<br>
      </ol>
      [code](https://github.com/madhuragandhe/Image_Processing/blob/master/Basics_Concepts/ImageResolution.py)<br>
      
  **3. Converting Color Space**<br>
       <ol>
          - We use the *color* class of the *skimage* module.<br>
          - We use different functions from the class, like: ***rgb2hsv, xyz2rgb, yiq2rgb***<br>
          - We use matplotlib to plot multiple figures together.<br>
      </ol>
      [code](https://github.com/madhuragandhe/Image_Processing/blob/master/Basics_Concepts/ColorSpace.py)<br>
      
  **4. Saving an Image**<br>
  
  **5.*
  **6. Brasic Drawing
  **7.
  **8.
  **9.
