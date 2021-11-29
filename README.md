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

##**Results**

Training Metrics 

Classifier	CV_Accuracy Mean	CV_Accuracy Std	CV_Bal_Accuracy Mean	CV_Bal_Accuracy Std	CV_f1_weighted Mean	V_f1_weighted Std
BaggingClassifier	0.525976	0.023871	0.450277	0.045487	0.515576	0.032943
LogisticRegression	0.51806	0.029768	0.471455	0.043051	0.514901	0.031016
XGBClassifier	0.47742	0.032557	0.422372	0.043924	0.471197	0.034774
RandomForestClassifier	0.460541	0.029992	0.403935	0.030446	0.454523	0.027347
CatBoostClassifier	0.454859	0.021424	0.406586	0.016917	0.451043	0.020593
SVC	0.433403	0.013816	0.388744	0.024309	0.429489	0.011903
![image](https://user-images.githubusercontent.com/34972681/143924587-ba80eac8-2732-44f0-b1f3-c71ef6650e9d.png)


