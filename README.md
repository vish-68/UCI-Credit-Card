
# UCI Credit Card

Financial threats are displaying a trend about the credit risk of commercial banks as the
incredible improvement in the financial industry has arisen. In this way, one of the
biggest threats faces by commercial banks is the risk prediction of credit clients. The
goal is to predict the probability of credit default based on credit card owner's
characteristics and payment history.

## Data Analysis

In UCI dataset we have 24 features(including target 
variable) and 30000 records.

* ID: ID of each client
* LIMIT_BAL: Amount of given credit in NT dollars (includes individual and family/supplementary credit
* SEX: Gender (1=male, 2=female)
* EDUCATION: (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown)
* MARRIAGE: Marital status (1=married, 2=single, 3=others)
* AGE: Age in years
* PAY_0: Repayment status in September, 2005 (-2=no consumption,-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, … 8=payment delay for eight months, 9=payment delay for nine   months and above)
* PAY_2: Repayment status in August, 2005 (scale same as above)
* PAY_3: Repayment status in July, 2005 (scale same as above)
* PAY_4: Repayment status in June, 2005 (scale same as above)
* PAY_5: Repayment status in May, 2005 (scale same as above)
* PAY_6: Repayment status in April, 2005 (scale same as above)
* BILL_AMT1: Amount of bill statement in September, 2005 (NT dollar)
* BILL_AMT2: Amount of bill statement in August, 2005 (NT dollar)
* BILL_AMT3: Amount of bill statement in July, 2005 (NT dollar)
* BILL_AMT4: Amount of bill statement in June, 2005 (NT dollar)
* BILL_AMT5: Amount of bill statement in May, 2005 (NT dollar)
* BILL_AMT6: Amount of bill statement in April, 2005 (NT dollar)
* PAY_AMT1: Amount of previous payment in September, 2005 (NT dollar)
* PAY_AMT2: Amount of previous payment in August, 2005 (NT dollar)
* PAY_AMT3: Amount of previous payment in July, 2005 (NT dollar)
* PAY_AMT4: Amount of previous payment in June, 2005 (NT dollar)
* PAY_AMT5: Amount of previous payment in May, 2005 (NT dollar)
* PAY_AMT6: Amount of previous payment in April, 2005 (NT dollar)
* default.payment.next.month: Default payment (1=yes, 0=no)

## Approach

Our main goal is to check whether the credit card owner belongs
to the defaulter or non-defaulter category.

* Data Exploration : Exploring dataset using pandas,numpy,matplotlib and seaborn.
* Data visualization : Use Tableau Data visualizationtools and also Ploted graphs to get insights about dependend and independed variables.
* Model Selection I : Tested all base models to check the base accuracy. Also ploted and calculate Performance Metrics to check whether a model is a good fit or not.
* Model Selection II : After testing all base if some of them are not working properly then we have to do model tunning
* Pickle File : Selected model as per best accuracy and created pickle file using pickle library.
* Webpage & deployment : Created a webform that takes all the necessary inputs from user and shows output. After that I have deployed project on Herokuapp 
## Technologies Used

* Jupyter notebook, Spyder, VScode Is Used For IDE.
* For Visualization Of The Plots Matplotlib , Seaborn Are Used.
* Herokuapp is Used For Model Deployment.
* Front End Deployment Is Done Using HTML, CSS, Bootstrap.
* Flask is for creating the application server and pages.
* Git Hub Is Used As A Version Control System.
* os is used for creating and deleting folders.
* csv is used for creating .csv format file.
* numpy is for arrays computations and mathematical operations
* pandas is for Manipulation and wrangling structured data
* scikit-learn is used for machine learning tool kit
* pickle is used for saving model
* Logistic regression is used for LogisticRegression Implementation.
* SGD is used for SGDClassifier Implementation.
* K-Nearest Neighbors is used for KNeighborsClassifier Implementation.
* SVM is used for SVC Implementation.
* Decision Tree is used for DecisionTreeClassifier Implementation.
* Extra Trees is used for ExtraTreesClassifier Implementation.
* Random forest is used for RandomForestClassifier Implementation.
* Ada boost is used for AdaBoostClassifier Implementation.
* Gradient is used for GradientBoostingClassifier Implementation.
* XGboost is used for XGBClassifier Implementation
* Ensemble is used for VotingClassifier Implementation.
  
## Deployment

**Herokuapp Link:** https://uci-credit-card.herokuapp.com/
  
## Deployment

To Clone this project run

```bash
git clone https://github.com/vish-68/UCI-Credit-Card
```
Go to Project directory
```bash
cd UCI-Credit-Card
```
Install dependencies
``` bash
pip install -r requirements.txt
```  
Run the app.py
```bash
python app.py
```
## Conclusion
We have developed UCI Credit Card Predictive model which is capable for predicting wheater the card owner belongs
to the defaulter or non-defaulter category. In this dataset we have 24 features(including target variable).First step is to check wheater the dataset contain missing values or not. We don't have missing values in the dataset. Second step is to do some data visualization to get some insight from given data after handling missing values. We can plot Countplot for checking imbalanced dataset, Pairplot for undestanding data, Co-relation plot for auto-corelation and boxplot for outliers detection. So here we can handel some outliers but it is not mandatory here because we are not geting outliers we are getting real values. After doing data visualization we observed that the dependent variable is imbalanced so we have done upsampling for our target variable. Then we donot have any alpha-categorical we have numerical categorical variable and after that  we have to do scaling, we perform Standard Scalar(values lies between -3 to +3) and then we have to build ML model likes LogisticRegression, SGDClassifier, KNeighborsClassifier, SVR, DecisionTreeRClassifier, ExtraTreesClassifier, RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier, VotingClassifier, XGBClassifier. Out of all of them ExtraTeeClassifier and RandomForest was working good because Accuracy achieved – 93.40% and 92.48%. So here we can say ExtraTreeClassifier model is working good. Last step is model Deployment using Flask Framework. For model deployment we have to dump our model using pickle library and can save our model in .pkl or .sav extension
