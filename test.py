import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

#reading set from csv file as a data frame by pandas
iris = pd.read_csv("iris_csv.csv")

#separating data into 3 types of irises
iris_setosa=iris.loc[iris["class"]=="Iris-setosa"]
iris_virginica=iris.loc[iris["class"]=="Iris-virginica"]
iris_versicolor=iris.loc[iris["class"]=="Iris-versicolor"]

#writing test file with summary description of full set and each type of irises
with open("summary.txt", "a" ) as f:
    f.write("\t *** ANALYSIS OF A IRIS DATA SET ***")
    f.write("\n")
    f.write("\n")
    f.write("First rows of a data set : \n {}".format(iris.head()))
    f.write("\n")
    f.write("\n")
    f.write("Description of a data set of irises :\n {}".format(iris.describe()))
    f.write("\n")
    f.write("\n")
    f.write("Description of a variable of iris setosa : \n {}".format(iris_setosa.describe()))
    f.write("\n")
    f.write("\n")
    f.write("Description of a variable of iris virginica : \n {}".format(iris_virginica.describe()))
    f.write("\n")
    f.write("\n")
    f.write("Description of a variable of iris versicolor : \n {}".format(iris_versicolor.describe()))
    f.write("\n")


