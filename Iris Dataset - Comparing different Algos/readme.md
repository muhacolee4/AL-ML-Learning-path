![Image of the correlation plot ](https://github.com/muhacolee4/AL-ML-Learning-path/blob/main/Iris%20Dataset%20-%20Comparing%20different%20Algos/comparing%20iris%20dataset.png)

# Introduction
This project presents the performance evaluation of five machine learning algorithms on the Iris flower dataset. The aim of this study is to compare the classification accuracy of Decision Tree, Gaussian Naive Bayes, K-Nearest Neighbors, Random Forest, and Support Vector Machine algorithms on the Iris dataset.
# Data
The Iris dataset is a widely used dataset in machine learning, which consists of 150 samples with four features: sepal length, sepal width, petal length, and petal width. Each sample is labeled as one of three species of Iris flowers: Iris setosa, Iris versicolor, or Iris virginica.
# Model Building and Evaluation
To evaluate the performance of the algorithms, the dataset was split into a training set and a testing set using a 70:30 ratio. The training set was used to train the models, and the testing set was used to evaluate their accuracy.

The Decision Tree, Gaussian Naive Bayes, and Random Forest classifiers were implemented using Scikit-Learn library in Python. The K-Nearest Neighbors and Support Vector Machine classifiers were also implemented using Scikit-Learn library with default hyperparameters.

The accuracy scores for each algorithm on the testing set were as follows:

Decision Tree: 0.9666666666666667
Gaussian Naive Bayes: 0.9666666666666667
K-Nearest Neighbors: 0.9833333333333333
Random Forest: 0.9833333333333333
Support Vector Machine: 0.9666666666666667
Based on the accuracy scores, the K-Nearest Neighbors and Random Forest classifiers achieved the highest accuracy of 0.9833333333333333, while the Decision Tree and Gaussian Naive Bayes classifiers achieved an accuracy of 0.9666666666666667, and the Support Vector Machine classifier achieved an accuracy of 0.9666666666666667.
# Conclusion
In conclusion, the results of this study demonstrate that the K-Nearest Neighbors and Random Forest classifiers are the most suitable algorithms for classification of Iris flowers among the tested algorithms. However, it is worth noting that the choice of algorithm depends on the specific problem and dataset, and it is always recommended to try multiple algorithms before making a final decision.