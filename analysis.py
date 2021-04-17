import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

#description of the dataset part as a full set 
irises = pd.read_csv("iris_csv.csv")
#separating data into 3 types of irises
iris_setosa=irises.loc[irises["class"]=="Iris-setosa"]
iris_virginica=irises.loc[irises["class"]=="Iris-virginica"]
iris_versicolor=irises.loc[irises["class"]=="Iris-versicolor"]

#writing test file with summary description of full set and each type of irises
with open("summary.txt", "a" ) as f:
    f.write("\t *** ANALYSIS OF A IRIS DATA SET ***")
    f.write("\n")
    f.write("\n")
    f.write("First rows of a data set : \n {}".format(irises.head()))
    f.write("\n")
    f.write("\n")
    f.write("Description of a data set of irises :\n {}".format(irises.describe()))
    f.write("\n")
    f.write("\n")
    f.write("Description of a variable of irises setosa : \n {}".format(iris_setosa.describe()))
    f.write("\n")
    f.write("\n")
    f.write("Description of a variable of irises virginica : \n {}".format(iris_virginica.describe()))
    f.write("\n")
    f.write("\n")
    f.write("Description of a variable of irises versicolor : \n {}".format(iris_versicolor.describe()))
    f.write("\n")#print(irises.describe())
#print(irises.index)
#print(irises.head())
#print(irises.head())


#scatter plot for compering sepal length and width of 3 classes of irises
sns.set_style("whitegrid")
sns.FacetGrid(irises, hue="class", height=4).map(plt.scatter, "sepallength", "sepalwidth").add_legend()
plt.show()
#scatter plot for comparing petal length and width of 3 classes of irises
sns.set_style("whitegrid")
sns.FacetGrid(irises, hue="class", height=4).map(plt.scatter, "petallength", "petalwidth").add_legend()
plt.show()


#coda that making histograms for all set of variables ( ), and write them to a files ( png)
iris_setosa=irises.loc[irises["class"]=="Iris-setosa"]
iris_virginica=irises.loc[irises["class"]=="Iris-virginica"]
iris_versicolor=irises.loc[irises["class"]=="Iris-versicolor"]
sns.FacetGrid(irises,hue="class",height=3).map(sns.distplot,"petallength").add_legend().savefig("petallength.png")
sns.FacetGrid(irises,hue="class",height=3).map(sns.distplot,"petalwidth").add_legend().savefig("petalwidth.png")
sns.FacetGrid(irises,hue="class",height=3).map(sns.distplot,"sepallength").add_legend().savefig("sepallength.png")
sns.FacetGrid(irises,hue="class",height=3).map(sns.distplot,"sepalwidth").add_legend().savefig("sepalwidth.png")
#plt.show()

