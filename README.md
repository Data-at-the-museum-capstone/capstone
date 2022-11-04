# <a name="top"></a>DATA AT THE MUSEUM
![george_crossing_the_delaware](https://github.com/Data-at-the-museum-capstone/capstone/blob/main/george_w_words.PNG)

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

** Additionally, some of the columns above were transformed or encoded prior to modeling, creating ~50 more features.  The transformed column names are ommitted for brevity

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

### Initial Correlation Testing
We explored the correlation of features using Chi<sup>2</sup> testing to show which columns had the most imbalanced proportions of highlight objects.  

Correlation test takeaways:
Is_timeline_work, is_public_domain, gallery_number_0, object_Fragment, medium_None, as well as some specific departments and culture types will be worth investigating.

### Investigating Departments
Exploring whether departments contain inequal proportions of highlight objects with enough deviation to be significant

H<sub>0</sub>:  The count of values for each department will not be significantly different from each other in proportion

H<sub>a</sub>:  The count of values for each department will be significantly different from each other in proportion

Testing confirmed that we could reject the null hypothesis for some departments.  There are unequal porportions of highlights within The Libraries, European Paintings, Robert Lehman Collection, The Cloisters, The American Wing, Musical Instruments, and Modern and Contemporary Art.

In other departments, the null hypothesis could not be rejected.  Drawings and Prints, Asian Art, European Sculpture and Decorative Arts, Photographs,  and Greek and Roman Art had highlight items in expected proportions.



### Investigating Object type
Exploring whether certain object types contain inequal proportions of highlights with enough deviation to be significant

H<sub>0</sub>:  The count of values for each object type will not be significantly different from each other in proportion
  
H<sub>a</sub>:  The count of values for each object type will be significantly different from each other in proportion

Testing confirmed that we could reject the null hypothesis for some object types.  There are unequal porportions of highlights within Paintings and Miscellaneous Ojects

For other object types, the null hypothesis could not be rejected.  Books, Fragments, Kylix, Negatives, Pieces, and Prints had highlight items in expected proportions

### Exploring The Outliers in the Libraries
After observing an unexpectedly high rate of highlight items in the Libraries Department we explored further to see if there was a bias we could capture. 
By grouping features it was discovered that Library pieces that were highlighted were more likely to have more information on the piece, and were more skewed toward an American target audience (Culture Type:  American, Gallery:  American Wing)

### Using Unsupervised Learning
Using K-means clustering we were able to identify a cluster that had a strong positive correlation to objects identified as highlights.  The cluster contained items with no medium identified, American culture, object name of Painting, part of the 'timeline' exhibition, and belonging to a specific subset of specific departments.  We tested this using Chi<sup>2</sup> testing against the following hypothesis:
  
H<sub>0</sub>:  The proportion of highlights for the cluster is not significantly different from the proportion of highlights in the overall population
  
H<sub>a</sub>:  The proportion of highlights for the cluster is significantly different from the proportion of highlights in the overall population

The test results allowed us to reject our null hypothesis.  In addition to this being a good feature for modeling, the few items in this cluster that are not highlights would be items that possibly should be.

### Takeaways from exploration:
- We identified some factors that drive highlights, used unsupervised learning to segment portions of our data, and created some features to carry forward to our model

[[Back to top](#top)]

***

## <a name="model"></a>Modeling:
  
Our target variable, is_highlight, is only true for .5% of items in the dataset.  

First tested using ###### model with ##### features and %%%%% parameters
  
#### Training Dataset (fill in actual results here)
| Model | Accuracy | f1 score |
| ---- | ---- | ---- |
| Baseline | 0.74| N/A |
| K-Nearest Neighbor | 0.80 | 0.53 |     
| Random Forest | 0.81 | 0.58 |  
| Logistic Regression | 0.80 | 0.60 |  

#### Validation Dataset (fill in actual results here)
| Model | Accuracy | f1 score |
| ---- | ---- | ---- |
| Baseline | 0.74| N/A |
| K-Nearest Neighbor | 0.78 | 0.47 |  
| Random Forest | 0.79 | 0.53 |  
| Logistic Regression | 0.78 | 0.56 |  


- The Second Model
  
  ###### Fill in data here

## Testing the Model

-  Results on Test Data

#### Testing Dataset (fill in actual results here)
             precision    recall  f1-score   support

           0       0.85      0.90      0.87      1035
           1       0.66      0.56      0.61       374

    accuracy                           0.81      1409     
    macro avg      0.76      0.73      0.74      1409
    weighted avg   0.80      0.81      0.80      1409

[[Back to top](#top)]

***

## <a name="conclusion"></a>Conclusion and Next Steps:

- Our model showed limited ability to predict whether or not an item is a significant 'highlight' work, which shows that judging art is in the eye of the beholder and not so much in data.



[[Back to top](#top)]

*** 

## <a name="reproduce"></a>Steps to Reproduce:

  - Download the wrangle.py, explore.py and final notebook files from this repository
  - Download the latest data csv from <a href="https://github.com/metmuseum/openaccess" target="_blank">The Metropolitan Museum's Open Access Site
  - Run the final_report.ipynb notebook

[[Back to top](#top)]
