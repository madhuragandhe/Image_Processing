<h2> Image Processing using Machine Learning concepts</h2>
  
1.**SIFT**: Feature mapping using Scale Invariant Feature Transform(SIFT) algorithm<br>
            SIFT algorithm is used to find similarities between two images.
            SIFT algorithm is a scale-invariant, which means that no matter how much we zoom in on the image,we can still find similarities.ANother feature of this algorithm is               that it is rotation invariant. Regardless of the degree of rotation, it still performs well.<br>
            Features of the image that the SIFT algorithm tries to factor out during processing are:
            <ol>
             ->Scale(zoomed-in or zoomed-out images)<br>
             ->Rotation<br>
             ->Illumination<br>
             ->Perspective<br>
            </ol>
            Lets look at step-by-step processof using the SIFT algorithm<br>
            <ol>
              1.Find and constructing a space to ensure scale invariance<br>
              2.Find the difference between the gaussians<br>
              3.Find the important points present inside the image<br>
              4.Remove unimportant points to make efficient comparisons<br>
              5.Provide orientation to the important points found in step3<br>
              6.Identifying the key features uniquely<br>
            </ol>
[code](https://github.com/madhuragandhe/Image_Processing/tree/master/MachineLearning_Concepts/SIFT)<br>

2.**RANSAC**: The process of putting one image over the other, at exactly the same place where it si present, is called *image registration*.<br>
              RANSAC consists of 4 steps:<br>
              <ol>
              1. Feature Detection and Extraction<br>
              2. Feature Matching<br>
              3. Transformation Function Fitting<br>
              4. Image Transformation and Image Resampling<br>
              </ol>
              The RANSAC algorithm is used in the thrid step to find the Transformation function.<br>
              We take two images and then,using the RANSAC algorithm,we find the homography(similarity) between those images.<br>
              <ol>
                1. <br>
                2.  <br>
              </ol>

[code](https://github.com/madhuragandhe/Image_Processing/tree/master/MachineLearning_Concepts/RANSAC)<br>
3.**Artificial Neural Networks**:<br>
[code]()
