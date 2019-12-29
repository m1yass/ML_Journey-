# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 18:38:36 2019

@author: maaro
"""

from sklearn import tree 

clf = tree.DecisionTreeClassifier()

clf2 = tree.DecisionTreeClassifier()


# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

Z = [25,20,18,16,19,30,20,21,22,23,24]
#to train the model 
clf = clf.fit(X, Y)

clf2 = clf2.fit(X,Z)

prediction = clf.predict([[190, 70, 43]])

prediction2 = clf2.predict([[190, 70, 43]])

print(prediction)
print(prediction2)