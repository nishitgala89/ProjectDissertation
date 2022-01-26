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

This is basic approach to train all the algorithms using the default class weight intialization. 
The Training and Evaluation metrics are as shown below and it is observed that neural network is the most efficient algorithm with higher accuracy, F1-score compared to all other algorithms. The classical ML model of Logistic regression outperforming the Boosting like XG Boost, Gradient Boosting and outperforming the Bagging algorithms like Random Forest and Bagging classifier. The confusion matrix for testing is shown in the figure 7.6 below. It clearly shows that majority of algorithms are performing well on the class 3, but not performing well on classes 1,5. Neural network model is performing exceedingly better on class 2,4 compared to other algorithms, whereas Bagging Classifier and Logistic regression are performing best on class 3.

![image](https://user-images.githubusercontent.com/34972681/151157292-c079c976-783e-4178-9c31-b65639472da4.png)

![image](https://user-images.githubusercontent.com/34972681/151157796-1d9f9ccc-5a3b-49e3-98f9-9f9aa54b4976.png)

![image](https://user-images.githubusercontent.com/34972681/151157841-24eb6516-fb6c-44a4-bbae-c6041d9ca48d.png)

As per the confusion matrix for model generalization, It is observed that the models are not generalizing well on class 1,2 with Neural Network model outperforming others. The Class 3, 4,5 has better prediction accuracy compared to class 1,2. It is also seen that almost all models performing well on class 3,4,5. Overall, the models are generalizing well with generalization metrics within the range of testing metrics. The only exception is Cat boost model that performs well only on class 4, and can choose to drop this model from the list of final models. Also, the generalization metrics for this algorithm is among the lowest. XG Boost algorithm is performing exceedingly well in predicting class 5 in the generalization test, however when looked upon testing metrics, it performs average in comparison to other models for the same class 5. These are some underlying issues that can be observed when comparing the generalization metrics with testing metrics. Logistic Regression, bagging classifier is the best algorithm in the generalization test for class 4, whereas Neural network model performs better in generalization test of class 3 compared to other algorithms.


### ***Approach 2: Models with Class weights***

This approach uses below formula for class weight initialization.<br/>                 
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; 𝑤𝑗=𝑛_𝑠𝑎𝑚𝑝𝑙𝑒𝑠 / (𝑛_𝑐𝑙𝑎𝑠𝑠𝑒𝑠 ∗ 𝑛_𝑠𝑎𝑚𝑝𝑙𝑒𝑠𝑗)<br/>
In the above formula, the n_samples refer to total training samples, n_classes is equal to 5 for the 5 rating of Morningstar and n_samplesj refers to the individual class sample count<br/>

The performance of the algorithms post class weight initialization does not better the final metrics when compared to no class weights initialization. The metrics are similar except there is a notable decrease in accuracy, F1-score in generalization test of Random Forest classifier post weight initialization. Also, the neural network performs better with class weight initialization than its predecessor model which is visible from testing and generalization metrics. The confusion matrix shows that all classifiers, except boosting classifiers, improved their performance on minority classes 1,5. Classifiers like neural networks, Logistic Regression, bagging classifier improved the prediction rate of minority classes significantly compared to Random Forest.

![image](https://user-images.githubusercontent.com/34972681/151164059-d8d27fa6-0fa9-469a-982e-b582c7b8b462.png)

![image](https://user-images.githubusercontent.com/34972681/151164194-7d973bf6-8366-470c-9e26-e263c97e71d4.png)

![image](https://user-images.githubusercontent.com/34972681/151164223-90d55c40-85e4-4787-a71c-d49a09c5c5ae.png)


### ***Approach 3: Stacked Model***
In this approach, a custom stacked model is built comprising of a stack of ML models like Random Forest, XG Boost, Gradient Boost, Logistic Regression, bagging classifier feeding into a Linear Regression model with the architecture as shown in the below figure. This model was built using the concept of feeding the ML model predictions to a Linear Regression model which will then be used as a single final predictor that combines the output of all models and provides an output as a decimal value which will be rounded up as the final prediction

![image](https://user-images.githubusercontent.com/34972681/151155733-fdf03076-abd7-41c9-9893-cfea2ab961e6.png)

The same approach was used as previous wherein the stacked model was trained for 5-Fold Cross validation and testing, generalizing check on all 5 folds. The linear regression model was trained by taking the predictions of all ML models as input and using the 5-fold CV training process to train it on the training data. The validation of the stacked model was performed on CV validation set, testing set, and generalization set (unseen data). This model did not perform better than individual neural network, Logistic regression or Bagging classifier models and the metrics are shown in the below table

![image](https://user-images.githubusercontent.com/34972681/151164542-48f4586a-36fd-435a-b81d-878adb93b7af.png)

![image](https://user-images.githubusercontent.com/34972681/151164621-5bedad85-546d-40f5-97cf-6c7ac4bd02f2.png)

The confusion metrics of the staked model show that they perform well on class 5 with the weighted model, and for all other classes the non-weighted model performs better. Overall, wanted to verify if the stacked model solution helps in better prediction for our problem statement. However, it’s not the case and the individual models outperform the stacked model in both testing and generalization checks.


***Approach 4: Target Class Reset***

The prediction capability of the model with 5 rating categories was around 45 to 55 %. This might be due to the limited feature selection as available on the Morningstar website in public domain. So, another method of reducing the target class to 3 ratings was tried as per below table

![image](https://user-images.githubusercontent.com/34972681/151156032-1a7fa105-5197-49e2-859b-16ce6f280ced.png)

The model evaluation and generalization checks are better compared to 5-class classification and hence, we can conclude that the ratings are more stable when categorized into 3 classes of Low, Medium, and High. The boosting algorithms are performing better compared to all other algorithms in evaluation on testing data, and unseen data. The results of model performance is shown in the below table

![image](https://user-images.githubusercontent.com/34972681/151165028-9b5fa4e8-4597-4bf4-912b-8bc26f46cc88.png)

The below figures are for the confusion matrix of Testing and Generalization checks. As observred, the accuracy and f1-score of the ML models are better with target reset and all the models perform well on classes 2,4. The class 3 has more inaccurate predictions compared to other classes 2,4 for all the algorithms. The generalization check of class 3 is poor for almost all the algorithms with all the model’s predicting majority of class 3 as class 4 in the generalization check as shown in figure 7.13. So, it can be concluded that the prediction rate of algorithms is better for class 2,4 and not good for the class 3 after the target class reset. Conversely, with 5 classes the prediction of the model was better on class 3 compared to other 4 classes.

![image](https://user-images.githubusercontent.com/34972681/151165348-0520f763-6ec7-4e34-9679-3e63fa057f9e.png)

![image](https://user-images.githubusercontent.com/34972681/151165390-a78c50e9-d9ab-4470-926d-83900ddea163.png)

## Conclusion

Before getting to the final models, a lot of parameters tuning and hyper parameter optimization using trial and run methods by changing parameters on the fly. Also, Grid Search and Randomized search options of Scikit-learn were explored to determine the best suitable hyper-parameters for the individual algorithms. The neural networks were trained with different optimizers, learning rate parameter tweaks, changes in the epochs and batch size etc. to determine the best possible network that performed well in both testing and generalization checks. The final models selected included Logistic Regression, Bagging Classifier, Random Forest, Gradient Boost, XG Boost, Neural Networks. It is observed that neural networks are the best in performance evaluation on the dataset in both testing and generalization checks when algorithms were trained without class weights. However, for model with class weights initialization the testing metrics showed the Bagging classifier as the best in testing. But in generalization checks, the neural network model outperformed the bagging classifier. Overall, the metrics indicated that model performed well without the weight’s initialization except for Neural network. The neural network outperformed all the models in both cases and was the best performing model by a gap of 4-5 percentage points for weight initialization training process. <br/>

An option of Stack model that is used most in the real-world applications was explored wherein, the model (Linear regression) takes input as the predictions of ML models and gives the final output as the combination of all the models. However, this did not work well with our dataset, and it was observed that individual ML algorithms performed better compared to the stacked model in both testing and generalization checks. <br/>

The accuracy score and F1-score metrics were in the range of 45-53% for the models and it did perform well compared to a normal guess in the rating which has a probability of 20% (1 out of 5 ratings). So, most of the ML models were at least 2 times better than the guess probability. One of the reasons for low performance of these models might be attributed to limited amount of data available from Morningstar in the public domain and there might be some techniques in the rating process which were not explored in this research as it was more focussed on predictions solely based on the information (data) available. <br/>

A target class reset was performed reducing the target size from 5 class ratings to 3 ratings (low, medium, and high) and it was observed that the ML algorithms were performing better at predicting the merged classes low (class 1,2) and high (class 4,5). However, the prediction capability of the medium class (class 3) was degraded when compared to 5 class target predictions. This research also indicated that the rating process on the purview of data at our disposal may be driven by some prejudices and bias as shown in the confusion matrix. There were overlaps among class predictions for all the classes and it is observe that algorithms were predicting high class for ground truth of low class and vice-versa. This can be attributed to limited amount of data available and techniques behind the manual rating process and its complexities. Another reason might be due to limited amount of mutual funds rated by Morningstar in UK, Europe-developed and Asia-Developed geographies. Overall, this research showed the ML algorithms can play important role in the ratings process of the Mutual Funds when provided with all important features and good amount of data for the training process. <br/>



