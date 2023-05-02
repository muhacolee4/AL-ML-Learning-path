# Title: Fine-Tuning K-Nearest Neighbors Classifier to Predict Diabetes
# Dataset
The dataset used in this project can be found in the diabetes.csv file (https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database). It contains 768 rows and 9 columns. The columns are as follows:

- Pregnancies: Number of times pregnant
- Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
- BloodPressure: Diastolic blood pressure (mm Hg)
- SkinThickness: Triceps skin fold thickness (mm)
- Insulin: 2-Hour serum insulin (mu U/ml)
- BMI: Body mass index (weight in kg/(height in m)^2)
- DiabetesPedigreeFunction: Diabetes pedigree function
- Age: Age (years)
- Outcome: Class variable (0 or 1) indicating whether a person has diabetes or not
# Prerequisites
- Python 3
- Scikit-learn
- Pandas
- Numpy
# Data Preprocessing
The following data preprocessing steps are performed before training the model:

- Replacing 0 values with the mean of the corresponding feature
- Splitting the dataset into training and testing sets
- Scaling the features using StandardScaler

# Model Building and Evaluation
A KNN classifier is built with k=11 and p=2 (Euclidean distance) using the training set. The model is evaluated on the testing set using F1 score and accuracy.

To improve the model's performance, hyperparameters are fine-tuned using GridSearchCV. The following hyperparameters are tuned:

n_neighbors: number of neighbors to consider
weights: function to weight the neighbors
p: distance metric (1 for Manhattan distance and 2 for Euclidean distance)
The best hyperparameters are found to be n_neighbors=15, weights='distance', and p=2. The model is trained using these hyperparameters and evaluated on the testing set. The performance of the tuned model is compared to the base model.


# Results
The confusion matrix, F1 score, and accuracy score of the base model and the tuned model are shown below.
## Base Model
- Confusion Matrix:
[[94 13]
 [21 26]]

- F1 Score: 0.5915492957746479

- Accuracy Score: 0.7727272727272727
## Tuned Model
- Confusion Matrix:
[[98  9]
 [22 25]]
F1 Score: 0.6136363636363635

- Accuracy Score: 0.7922077922077922

The tuned model performs slightly better than the base model with an increase of 2.1% in accuracy score and 3% in F1 score.