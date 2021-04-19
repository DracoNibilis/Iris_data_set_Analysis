import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

#reading set from csv file as a data frame by pandas
irises = pd.read_csv("iris_csv.csv")
print("WELCOME IN IRISES DATA ANALYTICS PROJECT\n")
print("Enter 1 - to see just 2 scatter plots of irises")
print("Enter 2 - to generate 4 histograms (show them / save them )")
print("Enter 3 - to get full raport (scatter / hist/ summary.txt file)")
print("Enter 4 - to quit")

list_of_choises = ["1", "2", "3", ]
choice = input()
#looping 
while choice in list_of_choises:
    if choice == "1":
        #do this 
        print("show scatters")
        choice = input()
        
    elif choice == "2":
        #do this
        print("show/save hist")
        choice = input()
    elif choice == "3":
        # do this
        print("FULLLL")
        choice = input()
else:
    print("program terminated")