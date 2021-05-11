**Step 1: Space Construction**<br>
<ol>
  1. Take original image and perform Gaussian blur, to remove unimportant points and extra noise<br>
  2. Resize the image and repeat the process<br>
</ol><br>

**Step 2: Difference between the Gaussians**<br>
<ol>
  1. Take images from step 1 and find the difference between their values.<br>
  2. This makes the image scale invariant.<br>
</ol><br>

**Step 3: Important Points**<br>
<ol>
  1. The difference between the gaussians image is used to determine the local maxima and minima. The pixel is marked as key point if it is maximum or minimum among all its neighbors.<br>
  2. Find subpixel maxima/minima using the Taylor expansion.When subpixels are found, we try to find the maxima and minima again.<br>
  3. To only take corners and consider them as key points, we use Hessian Matrix. Corners are always considered the best key points.<br> 
</ol><br>

**Step 4: Unimportant key points**<br>
<ol>
  1. Determine the threshold value.<br>
  2. In the key-ppoints generated image and the subpixels image check the pixel intensity with the threshold value.<br>
  3. If pixel intensity less than the threshold,we consider them unimportant points and reject them.<br>
</ol>

**Step 5: Orientation of Key points**<br>
<ol>
  1. Find direction of the gradient and the magnitude for each key point and its neighbors<br>
  2. Look at the most prevalent orientation around the key points and assign the same<br>
  3. We use histograms to do the same<br>
</ol>

**Step 6: Key Features**<br>
<ol>

2
</ol>

[sift_operations](https://github.com/madhuragandhe/Image_Processing/blob/master/MachineLearning_Concepts/SIFT/sift_operations.py)
