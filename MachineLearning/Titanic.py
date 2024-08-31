import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import sys

df = pandas.read_csv("MachineLearning\Titanic.csv")

d = {"male":0,"female":1}
df["Sex"]=df["Sex"].map(d)

d = {"S":0,"Q":1,"C":2}
df["Embarked"]=df["Embarked"].map(d)

new_df = df.drop(df.columns[[0,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25]], axis=1)

new_df = new_df.dropna()

print(new_df)

features = ["Pclass","Sex","Age","Embarked"]

X = new_df[features]
y = new_df["Survived"]

print(X)
print(y)

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
plt.figure(figsize=(12,12))
tree.plot_tree(dtree, feature_names=features,fontsize=3)

#plt.show()
print(dtree.predict([[2,0,35,1]]))
