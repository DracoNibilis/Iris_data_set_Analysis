import pandas as pd 
'''frame = pd.read_csv("iris_csv.csv")
#print(frame.head())
#print(frame.describe())
test_frame = frame.sort_values(by="class")
print(test_frame.head())'''

#change index for "class"
class_index = pd.read_csv("iris_csv.csv", index_col="class")
print(class_index.tail(20))

