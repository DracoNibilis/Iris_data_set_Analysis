import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

iris = pd.read_csv("iris_csv.csv")
#print(frame.head())


#coda that making histograms for all set of variables ( ), and write them to a files ( png)
iris_setosa=iris.loc[iris["class"]=="Iris-setosa"]
iris_virginica=iris.loc[iris["class"]=="Iris-virginica"]
iris_versicolor=iris.loc[iris["class"]=="Iris-versicolor"]
sns.FacetGrid(iris,hue="class",height=3).map(sns.distplot,"petallength").add_legend().savefig("petallength.png")
sns.FacetGrid(iris,hue="class",height=3).map(sns.distplot,"petalwidth").add_legend().savefig("petalwidth.png")
sns.FacetGrid(iris,hue="class",height=3).map(sns.distplot,"sepallength").add_legend().savefig("sepallength.png")
sns.FacetGrid(iris,hue="class",height=3).map(sns.distplot,"sepalwidth").add_legend().savefig("sepalwidth.png")
#plt.show()

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
#description of the dataset part as a full set 
frame = pd.read_csv("iris_csv.csv")
#print(frame.describe())
#print(frame.index)
#print(frame.head())
#print(frame.head())


#scatter plot for compering sepal length and width of 3 classes of irises
sns.set_style("whitegrid")
sns.FacetGrid(frame, hue="class", height=4).map(plt.scatter, "sepallength", "sepalwidth").add_legend()
plt.show()
#scatter plot for compering petal length and width of 3 classes of irises
sns.set_style("whitegrid")
sns.FacetGrid(frame, hue="class", height=4).map(plt.scatter, "petallength", "petalwidth").add_legend()
plt.show()