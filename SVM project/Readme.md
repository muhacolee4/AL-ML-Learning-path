# SVM Classification using ImageDataGenerator and Keras
This code implements a Support Vector Machine (SVM) classifier using Keras and the ImageDataGenerator class. The SVM classifier is trained on image data to classify images as containing or not containing a certain object.
## Data Source
The data is gotten from Kaggle (https://www.kaggle.com/chetankv/dogs-cats-images)
## Required Libraries
TensorFlow
Pandas
NumPy

Importing Libraries
The code starts by importing the required libraries. Tensorflow, Pandas, and NumPy are imported to perform numerical operations on the dataset. ImageDataGenerator from the Keras library is imported to perform data augmentation on the images.

Loading Data
The directory paths to the training and testing datasets are defined. The code creates data generators for training and testing using ImageDataGenerator. The train_datagen object applies various data augmentation techniques to the training images to help the model generalize better to new images. The rescale parameter rescales the pixel values of the images to be between 0 and 1, which is a common preprocessing step in deep learning. The shear_range, zoom_range, and horizontal_flip parameters are used to randomly apply shear, zoom, and horizontal flipping transformations to the images during training.

## Model Development
The code defines a CNN model using the Keras Sequential API. The model architecture consists of two 2D convolutional layers followed by two max pooling layers. The output of the second max pooling layer is flattened into a 1D vector and passed through two dense layers. The final dense layer has one neuron with linear activation and L2 regularization. This architecture is suitable for binary classification tasks, where the goal is to predict a binary outcome, such as whether an image contains a certain object or not.

## Compiling
The model is compiled using the Adam optimizer and the squared hinge loss function. The accuracy metric is used to evaluate the performance of the model.

## Training
The model is trained using the fit method of the Sequential object. The training data and validation data are passed as arguments, along with the number of epochs. The history object is used to track the training and validation accuracy and loss for each epoch.

## Requirements
To run this code, you need to have the following libraries installed:

TensorFlow
Pandas
NumPy
Keras
Note
The paths for the training and testing datasets are hard-coded in this code. You need to modify them to match the directory paths on your system.