################################################
#About 
#Date: Aug 22, 2016
#Store VCF File contents in a CSV file
##source: http://stackoverflow.com/questions/28043834/attributeerror-list-object-has-no-attribute-close-for-reading-one-file
################################################
import requests, re, sqlite3
from pyquery import PyQuery
from collections import Counter
import os
import glob
import pandas as pd 

aCHROM = []
bPOS = []
cID = []
dREF = []
eALT = []
fQUAL = []
gFILTER = []
hINFO = []
iFORMAT = []
jFORMAT = []
kFORMAT = []
lFORMAT = []
#Studies = []
mFORMAT = []
nFORMAT = []
oFORMAT  = []
pFORMAT  = []
qFORMAT  = []
#samples = []
rFORMAT  = []
#PopulationSummary = []
sFORMAT  = []

infilename = "GIAB_H002_081716.txt"
with open(infilename, "r") as infile:
    line_list = infile.readlines()

# firstLine = line_list.pop(0) #removes the header(first line)
# line_list = line_list[:-1]#removes the last line
for line in line_list:
    a = line.split('\t')
    aCHROM1 = a[0]
    bPOS1 = a[1]
    cID1 = a[2]
    dREF1 = a[3]
    eALT1 = a[4]
    fQUAL1 = a[5]
    gFILTER1 = a[6]
    hINFO1 = a[7]
    iFORMAT1 = a[8]
    jFORMAT1 = a[9]
    kFORMAT1 = a[10]

    lFORMAT1 = a[11]
    #Studies1 = a[12]
    mFORMAT1 = a[13]
    nFORMAT1 = a[14]
    oFORMAT1 = a[15]
    pFORMAT1 = a[16]
    qFORMAT1 = a[17]
    #samples1 = a[18]
    rFORMAT1 = a[19]
    #PopulationSummary1 = a[20]
    sFORMAT1 = a[21]


    aCHROM.append(aCHROM1)
    bPOS.append(bPOS1)
    cID.append(cID1)
    dREF.append(dREF1)
    eALT.append(eALT1)
    fQUAL.append(fQUAL1)
    gFILTER.append(gFILTER1)
    hINFO.append(hINFO1)
    iFORMAT.append(iFORMAT1)
    jFORMAT.append(jFORMAT1)
    lFORMAT.append(lFORMAT1)
    mFORMAT.append(mFORMAT1)
    nFORMAT.append(nFORMAT1)
    oFORMAT.append(oFORMAT1)
    pFORMAT.append(pFORMAT1)
    qFORMAT.append(qFORMAT1)
    rFORMAT.append(rFORMAT1)
    sFORMAT.append(sFORMAT1)

    print bPOS1

df = pd.DataFrame({'a.CHROM': aCHROM, 
		'bPOS': bPOS, 
		'c.ID': cID, 
		'd.REF': dREF, 
		'e.ALT': eALT, 
		'f.QUAL': fQUAL, 
		'g.FILTER': gFILTER, 
		'h.INFO': hINFO, 
		'i.FORMAT': iFORMAT, 
		'j.FORMAT': jFORMAT, 
		'l.FORMAT': lFORMAT, 
		'm.FORMAT': mFORMAT, 
		'n.FORMAT': nFORMAT, 
		'o.FORMAT': oFORMAT, 
		'p.FORMAT': pFORMAT, 
		'q.FORMAT': qFORMAT, 
		'r.FORMAT': rFORMAT, 
		's.FORMAT': sFORMAT})
	# print (df.head(8))
df.to_csv('df33.csv')

