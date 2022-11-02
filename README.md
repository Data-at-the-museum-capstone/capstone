# <a name="top"></a>DATA AT THE MUSEUM
![]()

by: Geary Shenck, David Howell and Dan Churchill

<p>
  <a href="https://github.com/geary-shenck" target="_blank">
    <img alt="Geary" src="https://img.shields.io/github/followers/geary-shenck?label=Follow_Geary&style=social" />
  </a>
</p>

<p>
  <a href="https://github.com/David-Howell" target="_blank">
    <img alt="David" src="https://img.shields.io/github/followers/david-howell?label=Follow_David&style=social" />
  </a>
</p>

<p>
  <a href="https://github.com/DanChurchill" target="_blank">
    <img alt="Dan" src="https://img.shields.io/github/followers/DanChurchill?label=Follow_Dan&style=social" />
  </a>
</p>


***
[[Project Description](#project_description)]
[[Project Planning](#planning)]
[[Data Dictionary](#dictionary)]
[[Data Acquire and Prep](#wrangle)]
[[Data Exploration](#explore)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]
[[Steps to Reproduce](#reproduce)]
___



## <a name="project_description"></a>Project Description:
The purpose of this project is to have a purpose

Goal 1: This is the first Goal

Goal 2: This is the second Goal


[[Back to top](#top)]

***
## <a name="planning"></a>Project Planning: 


### Project Outline:
- Acquire data 
- Perform initial data exploration 
- Clean and prepare data 
- Clearly define 
- Establish a baseline accuracy.
- Train  models.
- Evaluate models 

- Document conclusions, takeaways, and next steps in the Final Report Notebook.

[[Back to top](#top)]
***

## <a name="dictionary"></a>Data Dictionary  

| Target Attribute | Definition | Data Type |
| ----- | ----- | ----- |
| is_highlight | True if the item has been classified as a significant work | bool |


---
| Feature | Definition | Data Type |
| ----- | ----- | ----- |
| customer_id | Unique id for each customer| string |
| senior_citizen| 1 if customer is a senior citizen | int |
| tenure | Months of tenure as a customer| int |
| monthly_charges| The customer's monthly bill| float |
| total_charges| The customer's total bills since they have been a customer| float|
| male | 1 if the customer is male | int |
| partner | 1 if the customer has a partner  | int |
| dependents | 1 if the customer has dependents | int |
| phone | 1 if the customer has phone service | int |
| paperless_billing | 1 if the customer has paperliess billing | int |
| multiple_lines_yes | 1 if the customer has multiple phone lines | int |
| online_security_no | 1 if the customer has internet but no online security | int |
| online_security_yes | 1 if the customer has online security add-on | int |
| online_backup_no | 1 if the customer has internet but no online backup | int |
| online_backup_yes | 1 if the customer has online backup | int |
| device_protection_no | 1 if the customer has internet but no device protection | int |
| device_protection_yes | 1 if the customer has device protection | int |
| tech_support_no | 1 if the customer has internet but no tech support | int |
| tech_support_yes | 1 if the customer has tech_support | int |
| streaming_tv_no | 1 if the customer has internet but no streaming tv | int |
| streaming_tv_yes | 1 if the customer has streaming tv | int |
| streaming_movies_no | 1 if the customer has internet but no streaming movies | int |
| streaming_movies_yes | 1 if the customer has streaming movies | int |
| contract_type_month-to-month | 1 if the customer has a month-to-month contract | int |
| contract_type_one_year | 1 if the customer has a one year contract  | int |
| contract_type_two_year | 1 if the customer has a two year contract | int |
| payment_type_bank_transfer_auto | 1 if the customer pays by automatic bank transfer | int
| payment_type_credit_card_auto | 1 if the customer pays automatically by credit card | int
| payment_type_electronic_check | 1 if the customer pays manually by electronic check | int
| payment_type_mailed_check | 1 if the customer pays manually by mailed check | int
| internet_type_dsl  | 1 if the customer has DSL internet service |  int
| internet_type_fiber_optic | 1 if the customer has fiber optic internet service | int
| internet_type_none | 1 if the customer has no internet | int
| addon_count | sum of how many internet service add-ons the customer has | int

[[Back to top](#top)]

***

## <a name="wrangle"></a>Data Acquisition and Preparation

Data is acquired from...  This returns a dataframe containing ... rows and ... columns of data

Preparation is performed using 

- transformations
- Conversions
    * NOTE: There was weird stuff
- Encoded categorical and binary columns using 1-hot encoding
- Renamed columns
- Created features
- Split Data into 80% Train, 20% Validate, and 20% Test using 'is_highlight' as stratification



[[Back to top](#top)]

![]()


*********************

## <a name="explore"></a>Data Exploration:

### First Testing
The first step was to

Correlation test takeaways:


### Exploring XXXX
The training data was split into subsets of those that did and did not have internet service to see which was more likely to churn. 




### Exploring YYY 
To explore why internet users were more likely to churn we then utilized the add-on_count column by using a $Chi^2$ test


### Exploring ZZZ
We saw 


### Takeaways from exploration:
- We took some things away

[[Back to top](#top)]

***

## <a name="model"></a>Modeling:

#### Training Dataset
| Model | Accuracy | f1 score |
| ---- | ---- | ---- |
| Baseline | 0.74| N/A |
| K-Nearest Neighbor | 0.80 | 0.53 |  
| Random Forest | 0.81 | 0.58 |  
| Logistic Regression | 0.80 | 0.60 |  

#### Validation Dataset
| Model | Accuracy | f1 score |
| ---- | ---- | ---- |
| Baseline | 0.74| N/A |
| K-Nearest Neighbor | 0.78 | 0.47 |  
| Random Forest | 0.79 | 0.53 |  
| Logistic Regression | 0.78 | 0.56 |  


- The Logistic Regression model performed the best


## Testing the Model

- Logistic Regression Results on Test Data

#### Testing Dataset
             precision    recall  f1-score   support

           0       0.85      0.90      0.87      1035
           1       0.66      0.56      0.61       374

    accuracy                           0.81      1409
    macro avg      0.76      0.73      0.74      1409
    weighted avg   0.80      0.81      0.80      1409

[[Back to top](#top)]

***

## <a name="conclusion"></a>Conclusion and Next Steps:

- We created classification model that was awesome

- Here's more

- But wait, there's even more

- Final ground-breaking finding

[[Back to top](#top)]

*** 

## <a name="reproduce"></a>Steps to Reproduce:

You will need the source file and follow the :

  - Download the acquire.py, prepare.py, explore.py, and final_report.ipynb files
  - Add your own env.py file to the directory (user, host, password)
  - Run the final_repot.ipynb notebook

[[Back to top](#top)]
