# **ProjectDissertation - MorningStar Mutual Funds Rating prediction**

## **Introduction**
This project is a part of dissertation work as a student at Kingston University, London.
This is a supervised machine learning project wherein we are trying to predict the Mutual Funds rating given by Morningstar based on the features captured. The objective is to check if we can replicate Morningstar's rating process through ML techniques.
The ML algorithms used in the process are as listed below
1. Logistic Regression
2. Random Forest
3. Bagging Classifier with base estimator as Logistic Regression
4. SVM
5. XG Boost
6. Cat Boost
7. Artificial Neural Network
8. Voting Classifier

## **Steps involved in the Project**
1. Data Collection - Data is collected for equity Mutual Funds across UK, Europe developed and Asia develeoped geographies from Morningstar UK website. We have used Selenium for Web Scrapping the data from Morningstar.
2. Data Preparation - The Data is then prepared to remove the duplicate funds and cleansed using missing value, replacement, dropping un-necessary features, creating new features using feature engineering
3. Modelling - We have used the above listed Models to predict the Mutual Fund Ratings. In modelling, we have used 5-fold cross validation to check on Overfitting

## **Challenges Faced**

1. We faced the Overfitting issue initially wherein the training accuracy was very high (70-80%) and testing accuracy was very low (45-55%). So it was clear that model was overfitting to the training data.
2. We observed that the original dataset had same funds repeated multiple times with different names but with same ratings from Morningstar, so we need to consider only 1 fund amond the group of funds for Modelling. We have used below groupby to identify the similar funds and then used the index from group by dataframe to remove the duplicate records.
3. We performed modelling again and observed that Overfitting was gradually reduced and testing accuracy was nearby with training accuracy, but still we were seeing the model was overfitting to the training data.
4. To check on overfitting,  We also ensured that dataset is divided into manual split of 75-25 wherein the top 75% data was used for Training and bottom 25% was used for Testing. After this step, we observed that all models was generalizing well and we were getting similar testing and training accuracy.
5. Additionally, We also tried to perform oversampling of low frequency classes, however that did not help with overfitting.

## **Results**

**Part 1 - We have used the CV- 5fold cross validation**

***Training Metrics*** 

![image](https://user-images.githubusercontent.com/34972681/143924587-ba80eac8-2732-44f0-b1f3-c71ef6650e9d.png)


***Testing Metrics***

![image](https://user-images.githubusercontent.com/34972681/143924729-f40af0fc-5fc5-4678-9f6b-351711048d02.png)


***Confusion Matrix***

![image](https://user-images.githubusercontent.com/34972681/143926146-dbc110f4-35e6-46ac-b7fd-cd024cc18510.png)


***Model Generalization Check with Unseen data***

![image](https://user-images.githubusercontent.com/34972681/143924837-51e11167-df14-4787-84f1-7590eaa6e216.png)




