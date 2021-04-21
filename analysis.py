import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

#load dataset from csv file to pandas
irises = pd.read_csv("iris_csv.csv")
#separating data into 3 types of irises
iris_setosa=irises.loc[irises["class"]=="Iris-setosa"]
iris_virginica=irises.loc[irises["class"]=="Iris-virginica"]
iris_versicolor=irises.loc[irises["class"]=="Iris-versicolor"]

#creating text file summary.txt 
f = open("summary.txt", "a+")

#function that show scatter plots 2
def show_scatter(irises):
    sns.set_style("whitegrid")
    sns.FacetGrid(irises, hue="class", height=4).map(plt.scatter, "sepallength", "sepalwidth").add_legend()
    #plt.show()
    #sns.set_style("whitegrid")
    sns.FacetGrid(irises, hue="class", height=4).map(plt.scatter, "petallength", "petalwidth").add_legend()
    #plt.show()
    return plt.show()

#function that write to file -  histograms 4
def write_hist(irises):
    sns.FacetGrid(irises,hue="class",height=3).map(sns.distplot,"petallength").add_legend().savefig("petallength.png")
    sns.FacetGrid(irises,hue="class",height=3).map(sns.distplot,"petalwidth").add_legend().savefig("petalwidth.png")
    sns.FacetGrid(irises,hue="class",height=3).map(sns.distplot,"sepallength").add_legend().savefig("sepallength.png")
    sns.FacetGrid(irises,hue="class",height=3).map(sns.distplot,"sepalwidth").add_legend().savefig("sepalwidth.png")


#function to write summary into txt file

def text_summary(f):
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
        f.write("\n")
        #more about total analysis of set / conclusions
    return f

irises = pd.read_csv("iris_csv.csv")
print("WELCOME IN IRISES DATA ANALYTICS PROJECT\n")
print("Enter 1 - to see just 2 scatter plots of irises")
print("Enter 2 - to generate 4 histograms (show them / save them )")
print("Enter 3 - to get full raport (scatter / hist/ summary.txt file)")
print("Enter 4 - to quit")

list_of_choises = ["1", "2", "3", ]
choice = input("enter number: ")
#looping 
while choice in list_of_choises:
    if choice == "1":
        #use show_scatter function
        print("show scatters")
        show_scatter(irises)
        choice = input("enter number: ")
        
    elif choice == "2":
        #use write_hist function
        print("show/save hist")
        write_hist(irises)
        choice = input("enter number: ")
    elif choice == "3":
        # generate text file summary.txt use text_summary function
        print("generate txt file")
        text_summary(f)
        choice = input("enter number: ")
else:
    print("program terminated")

