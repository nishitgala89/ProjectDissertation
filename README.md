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
3. Modelling -  a) The algortihms are trained on UK, Europe developed geographies and the generalization check on unseen data is performed using Asia Developed geography.
                b) The above listed algorithms are used to predict the Mutual Fund Ratings. In modelling, we have used 5-fold cross validation along with metrics like F1-                        score, Balanced Accuracy, Confusion Matrix to validate evaluation of models.

## **Challenges Faced**

1. The algorithms were underfitting to training data and this was due to leakage of data as there were similar funds with different ID’s causing the algorithms to perform        better in testing. Similar funds with unique ID were identified using Group by and removed from the dataset. This reduced the data leakage in testing and thereby reducing    the underfitting.
2. Identified the algorithms performing poorly on low frequency classes in a slightly imbalanced dataset by verifying the confusion matrix. With oversampling technique, the      performance metrics improved, however the model was overfitting to training set. 

## **Approach for building models**

***Approach 1: Models without Class weights***
This is the basic approach to train all the algorithms using the default class weight intialization. 

***Approach 2: Models with Class weights***
This approach uses below formula for class weight initialization

𝑤𝑗=𝑛_𝑠𝑎𝑚𝑝𝑙𝑒𝑠 / (𝑛_𝑐𝑙𝑎𝑠𝑠𝑒𝑠 ∗ 𝑛_𝑠𝑎𝑚𝑝𝑙𝑒𝑠𝑗)

In the above formula, the n_samples refer to total training samples, n_classes is equal to 5 for the 5 rating of Morningstar and n_samplesj refers to the individual class sample count

***Approach 3: Stacked Model***
In this approach, a custom stacked model is built comprising of a stack of ML models like Random Forest, XG Boost, Gradient Boost, Logistic Regression, bagging classifier feeding into a Linear Regression model with the architecture as shown in the below figure. This model was built using the concept of feeding the ML model predictions to a Linear Regression model which will then be used as a single final predictor that combines the output of all models and provides an output as a decimal value which will be rounded up as the final prediction

![image](https://user-images.githubusercontent.com/34972681/151155733-fdf03076-abd7-41c9-9893-cfea2ab961e6.png)


***Approach 4: Target Class Reset***

The prediction capability of the model with 5 rating categories was around 45 to 55 %. This might be due to the limited feature selection as available on the Morningstar website in public domain. So, another method of reducing the target class to 3 ratings was tried as per below table

![image](https://user-images.githubusercontent.com/34972681/151156032-1a7fa105-5197-49e2-859b-16ce6f280ced.png)


## **Results**

**Part 1 - We have used the CV- 5fold cross validation**

***Training Metrics*** 

![image](https://user-images.githubusercontent.com/34972681/143924587-ba80eac8-2732-44f0-b1f3-c71ef6650e9d.png)

***Aritificial Neural Network***

![image](https://user-images.githubusercontent.com/34972681/143927059-5159db0c-90a8-4c0b-9743-4806b0917d4a.png)

![image](https://user-images.githubusercontent.com/34972681/143927110-336c2a36-d58b-4aa1-aa1c-6c2d1c9e8b0a.png)



***Testing Metrics***

![image](https://user-images.githubusercontent.com/34972681/143924729-f40af0fc-5fc5-4678-9f6b-351711048d02.png)


***Confusion Matrix***

![image](https://user-images.githubusercontent.com/34972681/143926146-dbc110f4-35e6-46ac-b7fd-cd024cc18510.png)


***Model Generalization Check with Unseen data***

![image](https://user-images.githubusercontent.com/34972681/143924837-51e11167-df14-4787-84f1-7590eaa6e216.png)




