Housing Price Prediction Model
This project involves building a machine learning model to predict housing prices based on various factors such as the median income, housing median age, total rooms, and total bedrooms, etc. The project uses data from a housing dataset and implements the Linear Regression model to make predictions.

Technologies Used
Python
Pandas
Numpy
Matplotlib
Scikit-learn
Dataset
The dataset used for this project is the California Housing Prices dataset, which is a modified version of the original dataset from the StatLib repository.

Data Analysis
The project starts with importing the necessary libraries and loading the dataset. After loading, we analyze the data using df.describe() and df.info() to check for missing data and get some basic statistical information about the data.

The data visualization is performed using the df.hist() function to plot histograms of the data, and the matplotlib.pyplot library is used to display the plots.

Model Building
To build the prediction model, the LinearRegression model is used from the Scikit-learn library. The dataset is split into training and testing data using the train_test_split function, and the model is trained using the training data.

The trained model is tested and scored against the testing data using the model.score() function, which gives an accuracy score of 0.60.

Conclusion
The project demonstrates how to use Linear Regression to predict housing prices based on various factors. However, the accuracy score of the model is not very high, and the project can be further improved by using more advanced machine learning techniques and tuning the hyperparameters of the model.



