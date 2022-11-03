# <a name="top"></a>DATA AT THE MUSEUM
![]()

by: Geary Shenck, David Howell and Dan Churchill

<p>
  <a href="https://github.com/geary-shenck" target="_blank">
    <img alt="Geary" src="https://img.shields.io/github/followers/geary-shenck?label=Follow_Geary&style=social" />
  </a> &emsp; 



  <a href="https://github.com/David-Howell" target="_blank">
    <img alt="David" src="https://img.shields.io/github/followers/david-howell?label=Follow_David&style=social" />
  </a> &emsp;



  <a href="https://github.com/DanChurchill" target="_blank">
    <img alt="Dan" src="https://img.shields.io/github/followers/DanChurchill?label=Follow_Dan&style=social" />
  </a>
</p>


***
[[Project Description](#project_description)]
[[Project Outline](#outline)]
[[Data Dictionary](#dictionary)]
[[Data Acquire and Prep](#wrangle)]
[[Data Exploration](#explore)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]
[[Steps to Reproduce](#reproduce)]
___



## <a name="project_description"></a>Project Description:
The NY Metropolitan Museum classifies roughly 2400 of their 480,000 items as ‘Highlights’.  Our team used supervised and unsupervised learning techniques to determine what factors contribute to an item being a highlight, and created a model to predict whether an item in the collection should be identified as such.  This model could be used by the Met to determine what pieces to feature in upcoming exhibitions, or by other museums to identify what underappreciated items to request on loan for their galleries.


[[Back to top](#top)]

***
## <a name="outline"></a>Project Outline: 

- Data Acquisition from the Metropolitan Museum Open Access page
- Initial data exploration 
- Clean and prepare data
- Define what factors contribute to an artwork being a highlight
- Establish a baseline for evaluating model accuracy
- Create and train predictive models
- Evaluate models
- Document conclusions, takeaways, and next steps

[[Back to top](#top)]
***

## <a name="dictionary"></a>Data Dictionary  

| Target Attribute | Definition | Data Type |
| ----- | ----- | ----- |
| is_highlight | True if the item has been classified as a significant work | bool |


---
| Feature | Definition | Data Type |
| ----- | ----- | ----- |
| object_number | Unique id for each object| string |
| title | Title, identifying phrase, or name given to an object | string |
| is_timeline_work | True if object was in the 'Timeline of Art History' exhibit | bool |
| is_public_domain | True indicates an artwork in the Public Domain | bool |
| accessionyear | Year the artwork was acquired by the museum| int |
| portfolio | True if the object was part of a set or series of works | True |
| constituent_id | unique id for the constituent | object |
| artist_role | the role of the constituent (artist, maker, author, etc.  | object |
| artist_alpha_sort | constituent name in format first, last | object |
| artist_nationality | National, geopolitical, cultural, or ethnic origin of the constituent | object |
| artist_begin_date | Year of birth for the constituent | object |
| artist_end_date | Year of death for the constituent (9999 if living) | object |
| artist_gender | Gender of the constituent | object |
| has_artist_url | True if the constituent has a ULAN artist page | bool |
| object_begin_date | Year creation of the object began | int |
| country | Country where the artwork was created or found | object |
| classification | General term describing the artwork type | object |
| object_wikidata_url | URL for object's wikidata page| object |
| tags | Primary subject keyword tag associated with the object | object |
| object_wikidata_url_1_or_0 | 1 if the object has a wikidata URL | int |
| gallery_number | Gallery number where the object is currently displayed | int |
| department | The curatorial department responsible for the object | object |
| object_name | The physical type of the object | object |
| culture | Information about the culture, or people from which an object was created | object |
| credit_line | Source or origin of the artwork and the year the object was acquired  | object |
| medium | Materials that were used to create the artwork | object |

** Some of the columns above were transformed or encoded prior to modeling.  The transformed column names are ommitted for brevity

[[Back to top](#top)]

***

## <a name="wrangle"></a>Data Acquisition and Preparation

Data is acquired in .csv format from <a href="https://github.com/metmuseum/openaccess" target="_blank">The Metropolitan Museum's Open Access Site
  


This returns a dataframe containing 477804 rows and 54 columns of data

Preparation is performed using preparation functions contained in the wrangle.py file.  The following operations were performed: 

- lowercase and remove whitespace from all column names
- Removed insignificant columns, duplicate columns, or columns without valid values
- Many columns had mulitple values separated by a '|'.  In these cases we only kept the first entry, which was the primary value.
- Converted dates to retain only digits for the year
- Artist gender only contained Female designations, so imputed male or N/A based upon values in other columns
- Converted portfolio and similar columns from categorical columns to boolean to reduce dimensionality
- Created binary dummy columns for remaining categorical features 
- Split Data into 80% Train, 20% Validate, and 20% Test using our target variable 'is_highlight' for stratification



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
