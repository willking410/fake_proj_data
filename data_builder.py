#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 16:10:22 2023

@author: willking
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 17:11:49 2023

@author: willking
"""
import numpy as np
import pandas as pd
import datetime

def myRand(myArg,myLow,myHigh):
    return myArg * np.random.randint(myLow,myHigh) / 100

def getInitiative(inits):
    myInit = inits[np.random.randint(0,len(inits))]
    return myInit

def getMgr(mgrs):
    myMgr = mgrs[np.random.randint(0,len(mgrs))]
    return myMgr

def getStartDate(projYears):
    myStart = datetime.date(np.random.randint(projYears[0],projYears[1]) \
                            , np.random.randint(1,12),1)
    return myStart

# DEFINE FIELD DATA

inits = ["Alpha", "Bravo", "Charlie"]

startYears = [2015,2022]

mgrs = ["Reilly, Madalyn", "Mitchell, Anna", "Hammes, Jasper", "Glover, Adeline" \
    , "Veum, Rosalia", "Rolfson, Pearline", "Bernier, Brant", "Goodwin, Lou" \
    , "Mertz, Georgiana", "Jacobs, Chet", "Dickens, Raquel", "Koss, Bernie" \
    , "Grant, Berry", "Bergstrom, Luther", "Bailey, Alexie", "Pfeffer, Lou" \
    , "Auer, Margret", "Stehr, Sadye", "Altenwerth, Pedro", "Walker, Abigail"]

budgets = [25000,50000,100000]
    
data1 = []
data2 = []
data3 = []

# BUILD BASE INFO TABLE
    
for i in range (50):
    myData = [getInitiative(inits), (i+1), getMgr(mgrs)\
              , getStartDate(startYears).strftime('%m-%Y')]
    data1.append(myData)

projBaseInfo = pd.DataFrame(data1,columns=['Initiative', 'ProjID', 'ProjMgr', 'StartDate'])

# BUILD ANNUAL BUDGET TABLE

projBaseInfo = projBaseInfo.reset_index(drop = True)

for index, row in projBaseInfo.iterrows():
    myMonth = row['StartDate'].split("-")[0]
    myYear = row['StartDate'].split("-")[1]
    base = budgets[np.random.randint(0,len(budgets))]
    
    for i in range (int(myYear),2023):
        myBudget = base * np.random.randint(85,115) / 100
        if i == int(myYear):
            myBudget = (13 - int(myMonth))/12 * myBudget
        myBudget = round(myBudget,-3)
        myData = [row['ProjID'], i, int(myBudget)]
        data2.append(myData)

projAnnualInfo = pd.DataFrame(data2, columns=['ProjID', 'Year', 'AnnualBudget'])

#print(projAnnualInfo.dtypes)

# BUILD MONTHLY FINANCIALS

projAnnualInfo = projAnnualInfo.reset_index(drop = True)

for index, row in projAnnualInfo.iterrows():
    # CHECK IF BASE MONTH
    myStart = projBaseInfo[projBaseInfo['ProjID']==row['ProjID']]['StartDate'].values[0]
    myMonth = myStart.split("-")[0]
    myYear = myStart.split("-")[1]
    myAnnual = int(projAnnualInfo.loc[(projAnnualInfo['ProjID'] == row['ProjID']) \
                       & (projAnnualInfo['Year'] == int(myYear)),['AnnualBudget']].values[0][0])
    
    # if start year, start a month index
    startMonth = 1
    
    if int(row['Year']) == int(myYear):
        startMonth = int(myMonth)
    
    for i in range(startMonth,13):
        mySpend = round(myAnnual / 12 * (np.random.randint(90,105) / 100),-1)
        myData = [row['ProjID'], myYear, i, int(mySpend)]
        data3.append(myData)

projMonthlyInfo = pd.DataFrame(data3, columns=['ProjID', 'Year', 'Month','Spend'])

# EXPORT TABLES TO CSV

projBaseInfo.to_csv('projBaseInfo')
projAnnualInfo.to_csv('projAnnualInfo')
projMonthlyInfo.to_csv('projMonthlyInfo')