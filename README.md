# Image_classifier_deployment
## Overview Dataset
Dataset yang digunakan adalah sebuah gambar yang terdiri dari 3 kelas yaitu paper, rock, dan scissors dengan jumlah sebanyak 2520 data. Masing-maisng kelas dalam dataset mempunyai jumlah sebanyak 840 gambar.
## Preprocessing dan Modelling
- Splitting data : Training = 70%, Validation= 25%, Testing = 5%
- Augmentasi data dengan menggunakan ImageDataGenerator 
- Modeling menggunakan pretrained VGG19 :
  
  summary model :
  
  ![summary](https://github.com/zachraaa/Image_classifier_deployment/assets/71622728/2f0c2e9c-62d7-4819-9e7d-1565feea0300)

  graph loss dam accuracy model :

  ![download](https://github.com/zachraaa/Image_classifier_deployment/assets/71622728/b7e76563-1de8-4479-abe9-0434d6273c0f)

  evaluation matrix model :

  ![confusion](https://github.com/zachraaa/Image_classifier_deployment/assets/71622728/24aa637f-b804-42bb-aeae-e7fd7fe5b8fd)

## Predict Data

## Local Development

![deployment](https://github.com/zachraaa/Image_classifier_deployment/assets/71622728/46174efc-3b03-45db-be5c-d4d74c38c1ba)


