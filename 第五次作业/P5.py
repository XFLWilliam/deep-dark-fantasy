import urllib.request
import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree

# 读取CSV文件数据
filename = 'prac5.csv'
data = pd.read_csv(filename, sep=';')
# print(data)

employee = data[['Transportation expense', 'Distance from Residence to Work', 'Absenteeism time in hours', 'Work load Average/day ', 'Hit target']]
target = data[['Age']]

plt.scatter(data['Age'], data['Service time'])
plt.xlabel('Age')
plt.ylabel('Service time')
plt.show()

attributes_training = employee[employee.index % 2 != 0]
target_training = target[target.index % 2 != 0]
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(attributes_training,target_training)

attributes_test = employee[employee.index % 2 != 1]
# print attributes_test
actual_test = target[target.index % 2 != 1]
actual_test.index = range(370)

prediction = clf.predict(attributes_test)

prediction_df = pd.DataFrame({'prediction': prediction})
training_result = pd.concat([prediction_df,actual_test], axis=1)
count = 0
for i in range(0, len(training_result)):
    if training_result['Age'][i] != training_result['prediction'][i]:
        count += 1
print('Wrong percent: '+str(round((float(count)/len(training_result))*100,2))+"%")
