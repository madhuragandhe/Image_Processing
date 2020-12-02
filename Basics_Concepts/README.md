
  **1. Uploading and Viewing an Image** <br>
       We start by importing a module named *skimage* .To upload and view an image <br>
       we use the *io* class from the *skimage* module.We use the two function from <br>
       this class:<br>
       <ol>
           - *imread*: to read the image<br>
           - *imshow*: to show the image<br>
       </ol>
       [code](https://github.com/madhuragandhe/Image_Processing/blob/master/Basics_Concepts/Open_Close.py)<br>

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
       To save an image we use *imsave* function from the *io* class.<br>
       The first argument in the function includes the name of the file to which you want<br>
       to save the image, the second argument is the variable that contains the image.<br>
       [code](https://github.com/madhuragandhe/Image_Processing/blob/master/Basics_Concepts/SavingImage.py)

  **5. Creating Basic Drawings**<br>
       We use the *draw* class for drawing images.<br>
       1. Lines<br>
        <ol>
            - We use the *line* function to draw a simple line on an image. <br>
            - The first two parameters indiate the first point;the last two parameters indicate the second point.<br>
            - A line is drawn using these points.<br>
            - We can change the pixel values of the line so we are able to see the line on the image.<br>
        </ol>
       2. Rectangle<br>
        <ol>
           - To draw a rectangle we use the *polygon* function. <br>
           - We give the x and y coordinates, then define the width and height.<br> 
       </ol>
       3. Circle<br>
        <ol>
            - We use the *circle* function to draw a circle on an image. <br>
            - The first two parameters indiate the position of the circle inside the image;<br>
              the last argument indicates the radius.<br>
       </ol>
       4. Bezier Curve<br>
        <ol>
            - We use the *bezier_curve* function to draw a bezier curve on an image. <br>
            - We need to indicate the position of three or more control points that then shape the curve.<br>
            - The first six arguments are used to define the three points; the last argument defines the tension present in the line.<br>
       </ol>
       5. Ellipse<br>
        <ol>
            - We use the *line* function to draw a simple line on an image. <br>
            - The first two parameters indiate the first point;the last two parameters indicate the second point.<br>
            - A line is drawn using these points.<br>
            - We can change the pixel values of the line so we are able to see the line on the image.<br>
       </ol> 
       [code](https://github.com/madhuragandhe/Image_Processing/blob/master/Basics_Concepts/BasicDrawings.py)
  
  **6. **<br>
  **7.e
  **8.
  **9.
