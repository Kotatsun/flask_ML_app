# flask_ML_app


## OverView
![mnist_test](https://user-images.githubusercontent.com/26564897/214135619-1dbd5493-8056-4ae5-8a0b-e7b94af7fe9f.gif)

This library is intended to run python machine learning models using flask.


## Required
+ Docker version 20.10.14


## How to test

### Build the docker container
[Shell]

> cd flask_ML_app/build
> bash build.sh

### Run the flask server

[Shell]

> cd flask_ML_app
> bash run.sh

Access localhost:5000
 
### Upload test image
Drag and drop images to select and complete the upload.
 

## Contents

+ build  
includes dockerfiles and rewuirement

+ data  
includes mnist test images

+ templates  
includes html files

+ weights  
includes trained model weights

+ train.sh
shell script to train the NN model

+ run.sh
shell script to run the flask server
