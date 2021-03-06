#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.3, random_state=42)
clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
labels_pred = clf.predict(features_test)
acc = accuracy_score(labels_test,labels_pred)
precision = precision_score(labels_test,labels_pred)
recall = recall_score(labels_test,labels_pred)
print acc
print precision
print recall
count = 0
for i in range(len(labels_test)):
	if labels_pred[i] and labels_test[i]:
		count = count+1
print count






