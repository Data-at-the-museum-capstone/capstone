import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from xgboost import XGBRegressor, XGBClassifier, XGBRFClassifier


from sklearn.model_selection import cross_val_score, cross_validate
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import make_scorer, multilabel_confusion_matrix, classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import average_precision_score, precision_recall_curve, recall_score, precision_score, accuracy_score



# class models()

def prep_X_sets(X_train, X_validate, X_test):
    X = [X_train, X_validate, X_test]
    
    drop_these = ['object_number',
    'accessionyear',
    'constituent_id',
    'artist_role',
    'artist_alpha_sort',
    'artist_nationality',
    'artist_begin_date',
    'artist_end_date',
    'artist_gender',
    'object_begin_date',
    'country',
    'classification',
    #  'object_wikidata_url',
    'tags',
    #  'gallery_number',
    #  'department',
    #  'object_name',
    #  'culture',
    #  'credit_line',
    #  'medium',
    ]  

    for x in X:
        x.drop(columns= drop_these, inplace=True)

    return X

class make_model:
    def __init__(self, X, y, X_val, y_val, model_name, scoring_method= 'recall', maximum_depth= None, learning_rate = 1):
        self.train = [X, y]
        self.validate = [X_val, y_val]
        self.name = model_name
        self.scoring = scoring_method
        self.max_depth = maximum_depth

        if self.name.lower() == 'decision_tree':
            model = DecisionTreeClassifier(max_depth= maximum_depth, random_state=123)
        
        if model_name.lower() == 'xgbreg':
            model = XGBRegressor(objective= 'reg:logistic', random_state=123)

        if model_name.lower() == 'xgbclass':
            model = XGBClassifier(random_state=123, max_depth= maximum_depth)

        if model_name.lower() == 'xgbrf':
            model = XGBRFClassifier(learning_rate= learning_rate, random_state=123)

        self.model = model.fit(X,y)

        self.train_preds = self.model.predict(X).round().astype('int')
        self.val_preds = self.model.predict(X_val).round().astype('int')

        self.recall = {'train': recall_score(y, self.train_preds),
                        'validate': recall_score(y_val, self.val_preds)}

        self.precision = {'train': precision_score(y, self.train_preds),
                          'validate': precision_score(y_val, self.val_preds)}

        self.accuracy = {'train': accuracy_score(y, self.train_preds),
                         'validate': accuracy_score(y_val, self.val_preds)}


        self.confusion = {'train': confusion_matrix(y, self.train_preds),
                          'validate': confusion_matrix(y_val, self.val_preds)}

        self.report = {'train': classification_report(y, self.train_preds),
                        'validate': classification_report(y_val, self.val_preds)}

    def cross_trees(self, cv=5, tests= 20):

        if self.name == 'decision_tree':

            results = []

            for x in range(1,(tests + 1)):
                tree = DecisionTreeClassifier(max_depth=x, random_state=123)
                score = cross_validate(tree, self.train[0], self.train[1], cv=cv, scoring= self.scoring)['test_score'].mean()
                results.append([x, score])
                
            pd.DataFrame(results, columns = ['max_depth', self.scoring])\
            .set_index('max_depth').plot(xticks=range(1,21))
            plt.title(f'{self.scoring.capitalize()} vs Max Depth in Decision Tree')
            plt.show()

        else:
            return 'Only DecisionTreeClissifier models can give you a cross_tree() graph... :/'

    def test(self, X_test, y_test):
        self.test_preds = self.model.predict(X_test).round().astype('int')

        self.recall['test'] = recall_score(y_test, self.test_preds)

        self.precision['test'] = precision_score(y_test, self.test_preds)

        self.accuracy['test'] = accuracy_score(y_test, self.test_preds)

        self.confusion['test'] = confusion_matrix(y_test, self.test_preds)

        self.report['test'] = classification_report(y_test, self.test_preds)

