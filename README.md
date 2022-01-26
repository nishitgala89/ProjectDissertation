# **ProjectDissertation - MorningStar Mutual Funds Rating prediction**

## **Introduction**
This project is a part of dissertation work as a student at Kingston University, London.
This is a supervised machine learning project wherein the goal is to predict the Mutual Funds rating given by Morningstar based on the features captured.
The ML algorithms used in the process are as listed below
1. Logistic Regression
2. Random Forest
3. Bagging Classifier with base estimator as Logistic Regression
4. XG Boost
5. Gradient Boost
6. Artificial Neural Network
7. Voting Classifier

## **Steps involved in the Project**
1. Data Collection - Data is collected for equity Mutual Funds across UK, Europe developed and Asia develeoped geographies from Morningstar UK website. We have used Selenium    for Web Scrapping the data from Morningstar.
2. Data Preparation - The Data is then prepared to remove the duplicate funds and cleansed using missing value, replacement, dropping un-necessary features, creating new        features using feature engineering
3. Modelling - The above listed algorithms are used for Modelling.<br/>
a) The algortihms are trained on UK, Europe developed geographies and the generalization check on unseen data is performed using Asia Developed geography. <br/>
b) The above listed algorithms are used to predict the Mutual Fund Ratings. In modelling, we have used 5-fold cross validation along with metrics like F1-                        score, Balanced Accuracy, Confusion Matrix to validate evaluation of models.

## **Challenges Faced**

1. The algorithms were underfitting to training data and this was due to leakage of data as there were similar funds with different ID’s causing the algorithms to perform        better in testing. Similar funds with unique ID were identified using Group by and removed from the dataset. This reduced the data leakage in testing and thereby reducing    the underfitting.
2. Identified the algorithms performing poorly on low frequency classes in a slightly imbalanced dataset by verifying the confusion matrix. With oversampling technique, the      performance metrics improved, however the model was overfitting to training set. 

## **Approach for building models**

### ***Approach 1: Models without Class weights***

This is the basic approach to train all the algorithms using the default class weight intialization. 
The Training and Evaluation metrics are as shown below and it is observed that neural network is the most efficient algorithm with higher accuracy, F1-score compared to all other algorithms. The classical ML model of Logistic regression outperforming the Boosting like XG Boost, Gradient Boosting and outperforming the Bagging algorithms like Random Forest and Bagging classifier. The confusion matrix for testing is shown in the figure 7.6 below. It clearly shows that majority of algorithms are performing well on the class 3, but not performing well on classes 1,5. Neural network model is performing exceedingly better on class 2,4 compared to other algorithms, whereas Bagging Classifier and Logistic regression are performing best on class 3.

![image](https://user-images.githubusercontent.com/34972681/151157292-c079c976-783e-4178-9c31-b65639472da4.png)

![image](https://user-images.githubusercontent.com/34972681/151157796-1d9f9ccc-5a3b-49e3-98f9-9f9aa54b4976.png)

![image](https://user-images.githubusercontent.com/34972681/151157841-24eb6516-fb6c-44a4-bbae-c6041d9ca48d.png)

As per the confusion matrix for model generalization, It is observed that the models are not generalizing well on class 1,2 with Neural Network model outperforming others. The Class 3, 4,5 has better prediction accuracy compared to class 1,2. It is also seen that almost all models performing well on class 3,4,5. Overall, the models are generalizing well with generalization metrics within the range of testing metrics. The only exception is Cat boost model that performs well only on class 4, and can choose to drop this model from the list of final models. Also, the generalization metrics for this algorithm is among the lowest. XG Boost algorithm is performing exceedingly well in predicting class 5 in the generalization test, however when looked upon testing metrics, it performs average in comparison to other models for the same class 5. These are some underlying issues that can be observed when comparing the generalization metrics with testing metrics. Logistic Regression, bagging classifier is the best algorithm in the generalization test for class 4, whereas Neural network model performs better in generalization test of class 3 compared to other algorithms.


### ***Approach 2: Models with Class weights***

This approach uses below formula for class weight initialization.<br/>
                 
&emsp&emsp&emsp&emsp&emsp&emsp&emsp&emsp𝑤𝑗=𝑛_𝑠𝑎𝑚𝑝𝑙𝑒𝑠 / (𝑛_𝑐𝑙𝑎𝑠𝑠𝑒𝑠 ∗ 𝑛_𝑠𝑎𝑚𝑝𝑙𝑒𝑠𝑗)<br/>
In the above formula, the n_samples refer to total training samples, n_classes is equal to 5 for the 5 rating of Morningstar and n_samplesj refers to the individual class sample count<br/>

### ***Approach 3: Stacked Model***
In this approach, a custom stacked model is built comprising of a stack of ML models like Random Forest, XG Boost, Gradient Boost, Logistic Regression, bagging classifier feeding into a Linear Regression model with the architecture as shown in the below figure. This model was built using the concept of feeding the ML model predictions to a Linear Regression model which will then be used as a single final predictor that combines the output of all models and provides an output as a decimal value which will be rounded up as the final prediction

![image](https://user-images.githubusercontent.com/34972681/151155733-fdf03076-abd7-41c9-9893-cfea2ab961e6.png)


***Approach 4: Target Class Reset***

The prediction capability of the model with 5 rating categories was around 45 to 55 %. This might be due to the limited feature selection as available on the Morningstar website in public domain. So, another method of reducing the target class to 3 ratings was tried as per below table

![image](https://user-images.githubusercontent.com/34972681/151156032-1a7fa105-5197-49e2-859b-16ce6f280ced.png)


