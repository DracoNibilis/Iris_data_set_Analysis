import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# reading data from csv file as a pandas data frame with set index as a class
frame = pd.read_csv("iris_csv.csv", index_col="class")
#rename index
frame.index.name = "IRIS CLASS"
# grouping index into 3 groups ( flower names) - making multiindex
f1 = frame.index.to_series()
f2 = f1.groupby(f1).cumcount()
frame.index = [frame.index, f2]

#making variables by multiindex - 3 variables by flowers
irises = frame.groupby(by=["IRIS CLASS"]) # grouping data by index ( 3 types )
#print(irises.size())
#get group - making variables for separate iris types (3 types)
iris_setosa = irises.get_group("Iris-setosa")
iris_versicolor = irises.get_group("Iris-versicolor")
iris_virginica = irises.get_group("Iris-virginica")
#print(iris_setosa.head())
#print(type(iris_setosa))

#making histogram for each variables 
plt.title("IRIS SETOSA") # title
plt.figure()
iris_setosa.plot.hist() # basic histogram for first variable
plt.show()
