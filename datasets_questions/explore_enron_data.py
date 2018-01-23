#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
from __future__ import division

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print 'No.of enron_data:',len(enron_data)

print 'No.of features:',len(enron_data["SKILLING JEFFREY K"])

num = 0
for name in enron_data.keys():
	if enron_data[name]["poi"] == 1:
		num += 1
print 'No.of POI in the dataset:',num

for k, v in enron_data["SKILLING JEFFREY K"].items():
	print k,v

print 'SKILLING JEFFREY K',enron_data["SKILLING JEFFREY K"]["total_payments"]
print 'FASTOW ANDREW S',enron_data["FASTOW ANDREW S"]["total_payments"]
print 'LAY KENNETH L', enron_data["LAY KENNETH L"]["total_payments"]

numS = 0
numE = 0
numTP = 0
for name in enron_data.keys():
	if enron_data[name]["salary"] != "NaN":
		numS += 1
	if enron_data[name]["email_address"] != "NaN":
		numE += 1
	if enron_data[name]["total_payments"] == "NaN":
		numTP += 1

print 'numS',numS
print 'numE',numE
print 'numTP',numTP

print numTP/len(enron_data)

numTPPOI = 0
for name in enron_data.keys():
	if enron_data[name]["poi"]  == 1 and enron_data[name]["total_payments"] == "NaN":
		numTPPOI += 1
		
print numTPPOI		
print numTPPOI/num


