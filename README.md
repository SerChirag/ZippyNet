
# ZippyNet
A case study about Neural Networks and Compression. 

## Data-Set
We have used [Large-scale CelebFaces Attributes Dataset](Large-scale%20CelebFaces%20Attributes%20%28CelebA%29%20Dataset).
The reason for using this dataset was simply because the dataset was uniform. It contains 669 images of 42*42 dimension images of celebrities.
![Data-Set Example](https://lh3.googleusercontent.com/PAsvoRaTCuwllU-q_gjcMGGiwQZ1F-cxGHtd_bYw9l97Y5VLNXkG_eQkS77WuzfdlZlVejxtmp-D "Data-Set Example")

## Comparision with other image compressors:
Quality of image has been measured according to website: https://www.imgonline.com.ua/eng/determine-jpeg-quality.php

### Comparision with famous linux application mogrify to compress images.
Image | OriginalSize | CompressedSize | Quality
|--|--|--|--|
000001.jpg | 1kb | 1kb | 75
000002.jpg | 1kb | 1kb | 75

### Comparision with website https://compressimage.toolur.com/
Image | OriginalSize | CompressedSize | Quality
|--|--|--|--|
000001.jpg | 1kb | 1.2kb | 95
000002.jpg | 1kb | 1.2kb | 95

### Conclusion:
From the comparisions it is clear that tradional compression algorithms are not good at compressing smaller sized images. Either they are unable to further compress images(mogrify) or they increase the size of images, which is opposite of what we want. This provides use-case opportunities to application of deep learning for image compression.
