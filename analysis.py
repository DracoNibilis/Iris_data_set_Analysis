import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


frame = pd.read_csv("iris_csv.csv")
#print(frame.head())
#print(frame.describe())
test_frame = frame.sort_values(by="class")
#test_frame.rename(columns = {"class": "flower_class"})
#print(test_frame.head())
#print(test_frame.head())
#change index for "class"
#class_index = pd.read_csv("iris_csv.csv", index_col="class")
#print(class_index.tail(20))

#checking index and its value
#print(list(class_index.index))

#grupby data by variables ( 3 types of flowers) , convert column to type category
#print(test_frame['flower_class'].value_counts())
#declare variables for unique flower types 
irises = test_frame['class'].unique()
#print(irises)
flower_groups = {} # empty dictionary 
for flower in irises:
    sub_flower = test_frame.where(test_frame['class'] == flower).dropna()
    flower_groups[flower] = sub_flower
#print(flower_groups.keys())
#print(flower_groups['Iris-virginica'].head())

#making plot ( histogram ) for each variable
var_1 = pd.DataFrame(flower_groups['Iris-setosa'])
print(var_1)
var_1_n = np.array(var_1)
'''print(var_1_n)

plt.title("iris setosa")
plt.plot(var_1_n)

plt.legend()
plt.show()'''
