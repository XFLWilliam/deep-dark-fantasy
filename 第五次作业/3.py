from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import urllib.request
import pandas as pd
import numpy as np
from sklearn import tree

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
response = urllib.request.urlopen(url)
data = response.read()      # a raw bits 'bytes' object
text = data.decode('utf-8') # use the utf-8 string format to create a string 'str' object
iris_df=pd.read_csv(url, names=("sepal length","sepal width","petal length","petal width","class")) # Panda object
x = iris_df["sepal length"]
y = iris_df["petal length"]
z = iris_df["petal width"]
classes = iris_df["class"]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

colors = {'Iris-setosa':'red', 'Iris-virginica':'blue', 'Iris-versicolor':'green'}

for i in range(len(x)):
    ax.scatter(x[i], y[i], z[i], c=colors[classes[i]])

ax.set_xlabel('sepel length')
ax.set_ylabel('petal length')
ax.set_zlabel('petal width')

plt.show()



attributes = iris_df[["sepal length","sepal width","petal length","petal width"]]
target = iris_df[["class"]]

clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(attributes,target)

prediction = clf.predict(attributes)
prediction_df = pd.DataFrame({"prediction": prediction})
prediction_df.head()

# create a result that contains the training data classes and the prediction result
# use the pandas function concat to join the data frames - note the axis parameter means to join columns
training_result = pd.concat([prediction_df, target], axis=1)
training_result.head()

# misclassification
num_rows = training_result['prediction'].count()
num_incorrect = num_rows - sum(training_result['prediction'] == training_result['class'])
percentage = (num_incorrect/num_rows)*100
print(percentage)

