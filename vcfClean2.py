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

train = pd.read_csv("df34.csv")
print train.head()

def title(name):
    temp_1 = name.split('=')[1] # Split by (=)
    # temp_2 = temp_1[1].split('=')[0] # Split by (.)
    # temp_3 = temp_2.strip() # Remove white space
    return temp_1

train['SUPP'] = train['SUPP'].apply(title) # Apply function 'title' function to 'Frequency'
train['AVGLEN'] = train['AVGLEN'].apply(title)
train['SVTYPE'] = train['SVTYPE'].apply(title)
train['CHR2'] = train['CHR2'].apply(title)
train['END'] = train['END'].apply(title)

print (train['SUPP'])

train.to_csv('df35.csv')



