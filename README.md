


# ZippyNet
A case study about Neural Networks and Compression. 

## Data-Set
We have used [Large-scale CelebFaces Attributes Dataset](Large-scale%20CelebFaces%20Attributes%20%28CelebA%29%20Dataset).
The reason for using this data-set was simply because the data-set was uniform. It contains 669 images of 42*42 dimension images of celebrities.
![Data-Set Example](https://lh3.googleusercontent.com/PAsvoRaTCuwllU-q_gjcMGGiwQZ1F-cxGHtd_bYw9l97Y5VLNXkG_eQkS77WuzfdlZlVejxtmp-D "Data-Set Example")

## Comparison with other image compressors:
Quality of image has been measured according to website: https://www.imgonline.com.ua/eng/determine-jpeg-quality.php

### Comparison with famous linux application mogrify to compress images.
Image | OriginalSize | CompressedSize | Quality
|--|--|--|--|
000001.jpg | 1kb | 1kb | 75
000002.jpg | 1kb | 1kb | 75

### Comparison with website https://compressimage.toolur.com/
Image | OriginalSize | CompressedSize | Quality
|--|--|--|--|
000001.jpg | 1kb | 1.2kb | 95
000002.jpg | 1kb | 1.2kb | 95

### Conclusion:
From the comparisons it is clear that traditional compression algorithms are not good at compressing smaller sized images. Either they are unable to further compress images(mogrify) or they increase the size of images, which is opposite of what we want. This provides use-case opportunities to application of deep learning for image compression.

### Scope

**Relevance with respect to Data-Set**

Compression works best on high-dimensional images with little significance for relative positioning of objects within the data.
 
![enter image description here](https://thrivethemes.com/wp-content/uploads/2018/05/jpg-png-filesize-compressed.png)

Thus it works best for landscape like images. Shifting the mountain by a few pixels or changing the colour of the sky does not affect the image.

We have trained our data on a low-dimensional data-set with high importance to relative positioning of objects.Shifting the nose by a few pixels greatly impacts the out image. Hence, our model is extremely important as it is training on a very hard data-set and still giving excellent results.
<br>


**Scope of One-Model**

We tried to train a similar model on a [](https://data.vision.ee.ethz.ch/cvl/DIV2K/). This data-set contained random image ranging from various people, object, buildings etc. The resulting model did not train at all.
Thus, auto-encoders can be used as a compressor only for similar looking data-set, unlike other compression algorithms like JPEG and JPEG-2000.

<br>

**Representation of Compressed Form**

Currently, the compressed data obtained from the auto-encoder is stored as a '.npy' file, which is notorious for high overheads.
Thus, if we can effectively store the output of the auto-encoder, we will be further compress the image.



