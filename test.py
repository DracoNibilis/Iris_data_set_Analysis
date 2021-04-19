import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

#reading set from csv file as a data frame by pandas
irises = pd.read_csv("iris_csv.csv")

#function that show scatter plots 
def show_scatter(irises):
    sns.set_style("whitegrid")
    sns.FacetGrid(irises, hue="class", height=4).map(plt.scatter, "sepallength", "sepalwidth").add_legend()
    plt.show()
    sns.set_style("whitegrid")
    sns.FacetGrid(irises, hue="class", height=4).map(plt.scatter, "petallength", "petalwidth").add_legend()
    plt.show()


show_scatter(irises)



#function that write to file histograms
def write_hist(irises):
    sns.FacetGrid(irises,hue="class",height=3).map(sns.distplot,"petallength").add_legend().savefig("petallength.png")
    sns.FacetGrid(irises,hue="class",height=3).map(sns.distplot,"petalwidth").add_legend().savefig("petalwidth.png")
    sns.FacetGrid(irises,hue="class",height=3).map(sns.distplot,"sepallength").add_legend().savefig("sepallength.png")
    sns.FacetGrid(irises,hue="class",height=3).map(sns.distplot,"sepalwidth").add_legend().savefig("sepalwidth.png")


write_hist(irises)

