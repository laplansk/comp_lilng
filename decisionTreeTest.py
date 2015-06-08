import collections
from sklearn import tree
from sklearn import datasets

# dataset = datasets.load_iris()
# print dataset


# Samples
sample1 = "This is a Jack Jack Jack email that mentions Jill."
sample2 = "This is a Steve Steve Steve Steve email that mentions Jack once."
sample3 = "This is a Jill Jill Jill email that mentions Jack just once."
samples = [sample1, sample2, sample3]

#feature sets
# f1 = {"Jack" : 3, "Jill" : 1, "Steve" : 0}
f1 = [3, 1, 0]
# f2 = {"Jack" : 1, "Jill" : 0, "Steve" : 4}
f2 = [1, 0, 4]
# f3 = {"Jack" : 1, "Jill" : 4, "Steve" : 0}
f3 = [1, 4, 0]
features = [f1, f2, f3]

# gold classes
# outputs = ["Jack", "Jill", "Stephen"]
outputs = [0, 1, 2]

X = features
y = outputs

decisionTree = tree.DecisionTreeClassifier()
decisionTree.fit(X, y)

# test inddexing lists with nothing in them

listA = [0] * 10
listA[5] += 1
print listA





