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

[code](https://github.com/madhuragandhe/Image_Processing/tree/master/MachineLearning_Concepts/RANSAC)<br>
3.**Artificial Neural Networks**:<br>
[code]()
