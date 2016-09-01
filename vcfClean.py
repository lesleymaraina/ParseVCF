#################################################################
#About
#Date: July 18, 2016
#source: http://www.pythonlearn.com/html-008/cfbook009.html
#source: Udemy: Regex example program: a pone and email scraper
#source: https://www.youtube.com/watch?v=ve2pmm5JqmI
#################################################################

#################################################################
#Imports
#################################################################
import os
import glob
import pandas as pd 

#################################################################
#Code
#################################################################

train = pd.read_csv("df33.csv")
print train.head()

def title(name):
    temp_1 = name.split(';')[0] # Split by (=)
    # temp_2 = temp_1[1].split('=')[0] # Split by (.)
    # temp_3 = temp_2.strip() # Remove white space
    return temp_1
def title2(name):
    temp_1 = name.split(';')[1] # Split by (=)
    # temp_2 = temp_1[1].split('=')[0] # Split by (.)
    # temp_3 = temp_2.strip() # Remove white space
    return temp_1
def title3(name):
    temp_1 = name.split(';')[2] # Split by (=)
    # temp_2 = temp_1[1].split('=')[0] # Split by (.)
    # temp_3 = temp_2.strip() # Remove white space
    return temp_1
def title4(name):
    temp_1 = name.split(';')[3] # Split by (=)
    # temp_2 = temp_1[1].split('=')[0] # Split by (.)
    # temp_3 = temp_2.strip() # Remove white space
    return temp_1
def title5(name):
    temp_1 = name.split(';')[4] # Split by (=)
    # temp_2 = temp_1[1].split('=')[0] # Split by (.)
    # temp_3 = temp_2.strip() # Remove white space
    return temp_1
def title6(name):
    temp_1 = name.split(';')[5] # Split by (=)
    # temp_2 = temp_1[1].split('=')[0] # Split by (.)
    # temp_3 = temp_2.strip() # Remove white space
    return temp_1

train['SUPP'] = train['h.INFO'].apply(title) # Apply function 'title' function to 'Frequency'
train['AVGLEN'] = train['h.INFO'].apply(title2)
train['SVTYPE'] = train['h.INFO'].apply(title3)
train['SVTYPE'] = train['h.INFO'].apply(title4)
train['CHR2'] = train['h.INFO'].apply(title5)
train['END'] = train['h.INFO'].apply(title6)


print (train['SUPP'])

train.to_csv('df34.csv')



