# Spam Classification using Logistic Regression
This is a Python code for a spam classification system that can predict whether an email is spam or not using Logistic Regression.

Dependencies
The following dependencies are required to run the code:

- numpy
- pandas
- scikit-learn
# Data Collection & Pre-Processing
The data was gotten from https://github.com/akashdeep364/Spam-Mail-Prediction/blob/main/mail_data.csv. 
The code starts by loading the email data from a csv file into a pandas dataframe. It then prints out some information about the data, including the number of rows and columns, and any null values.

Next, the code replaces any null values with an empty string, and then performs label encoding to label spam emails as 0 and ham emails as 1.

Finally, the code splits the data into training and test sets, with a test size of 20%.

# Feature Extraction
The code then transforms the text data to feature vectors that can be used as input to the Logistic Regression model using the TfidfVectorizer function from scikit-learn.

# Training the Model
The code trains a Logistic Regression model with the training data, and then evaluates the model's accuracy on both the training and test data.

Building a Predictive System
Finally, the code includes a sample input email to demonstrate how the model can be used to predict whether an email is spam or not.

To use this code, you can replace the input email with your own text and run the code to see whether it is classified as spam or ham.



