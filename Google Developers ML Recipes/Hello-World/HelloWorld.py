#Scikit learn
from sklearn import tree

#Collect Training Data

#1 = smooth, 0 = bumpy
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
#0 = apple, 1 = orange
labels = [0, 0, 1, 1]

#Train the Classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
#fit - synonym, "Find patterns in data"

#Predict
res1 = clf.predict([[150, 0]])
res2 = clf.predict([[135, 1]])
res3 = clf.predict([[180, 0]])

#Helper
def intToFruit(val):
    if(val[0] == 1):
        print("Orange")
    else:
        print("Apple")

intToFruit(res1) #Orange
intToFruit(res2) #Apple
intToFruit(res3) #Orange
