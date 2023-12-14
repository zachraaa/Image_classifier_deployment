# Image_classifier_deployment
## Overview Dataset
Dataset yang digunakan adalah sebuah gambar yang terdiri dari 3 kelas yaitu paper, rock, dan scissors dengan jumlah sebanyak 2520 data. Masing-maisng kelas dalam dataset mempunyai jumlah sebanyak 840 gambar.
## Preprocessing dan Modelling
- Splitting data : Training = 70%, Validation= 25%, Testing = 5%
- Augmentasi data dengan menggunakan ImageDataGenerator 
- Modeling menggunakan pretrained VGG19 :
  summary model :
  ![summary](https://github.com/zachraaa/Image_classifier_deployment/assets/71622728/2f0c2e9c-62d7-4819-9e7d-1565feea0300)
  
