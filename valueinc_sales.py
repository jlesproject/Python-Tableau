#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 14:01:41 2024

@author: jamieleslie
"""

import pandas as pd

# file_name = pd.read_csv("file.csv") for <---- format of read_csv

data = pd.read_csv("transaction.csv")

data = pd.read_csv("transaction.csv", sep=";")

#summary of the data
data.info()

#playing around with variables

var =  True

#working with calculations

#defining variables

CostPerItem = 11.73
SellingPricerPerItem = 21.11
NumberofItemsPurchased = 6

#Mathematical Operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricerPerItem - CostPerItem
ProfitPerTransaction = NumberofItemsPurchased * ProfitPerItem
CostPerTransaction =  CostPerItem * NumberofItemsPurchased
SellPricePerTransaction = SellingPricerPerItem * NumberofItemsPurchased

#CostPerTransaction Column Calculation

#CostPerTransactoin = CostPerItem * NumberofItemsPurchased
# variable = dataframe["column_name"]

CostPerItem = data["CostPerItem"]
NumberofItemsPurchased = data["NumberOfItemsPurchased"]

CostPerTransaction = CostPerItem * NumberofItemsPurchased

#adding new column to a dataframe

data["CostPerTransaction"] = CostPerTransaction

#Sales per Transaction

data["SalesPerTransaction"] = data["SellingPricePerItem"] * NumberofItemsPurchased

#Profit Calculation = Sales - Cost

data["ProfitperTransaction"] = data["SalesPerTransaction"] - CostPerTransaction

#Markup = (Sales - Cost)/Cost

data["Markup"] = (data["SalesPerTransaction"] - CostPerTransaction )/ CostPerTransaction


#Rounding Markup

data["Markup"] = rounndmarkup = round(data["Markup"],2)


#combining data fields
#change columns type

day = data["Day"].astype(str)

my_date = day + '-' +(data['Month'].astype(str)) + '-' + (data['Year'].astype(str))

data["Date"] = my_date
#checking columns data type
print(data["Day"].dtype)

#using iloc to view specific columns/rows

data.iloc[0] #view the row with index = 0

data.iloc[0:4] #first 4 rows
data.iloc[-5:] #last 5 rows

data.head(5) #first 5 rows

data.iloc[:,2] #brings in all rows in second column

data.iloc[4,2] #4th row in the second column


#using split to split the client keywords field

#new_var = column.str.split('sep', expand = True)

split_col = data['ClientKeywords'].str.split(',', expand = True)

#creating new column for the split columns in Client Keywords

data["ClientAge"] = split_col[0]
data["ClientType"] = split_col[1]
data["LengthofContract"] = split_col[2]

#using the replace function
data["ClientAge"] = data["ClientAge"].str.replace("[", " ")
data["LengthofContract"] = data["LengthofContract"].str.replace("]", " ")

#using the lower function to change item to lowercase

data["ItemDescription"] = data["ItemDescription"].str.lower()

#how to merge files

#bringing in a new dataset

seasons = pd.read_csv("value_inc_seasons.csv", sep= ";")

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

seasons["Month;Season"] = split_col[0]

data = pd.merge(data, seasons, on = "Month")

#dropping columns
#df = df.drop("columnname" , axis = 1)

data = data.drop("ClientKeywords", axis = 1)

data = data.drop("Day", axis = 1)

data = data.drop(['Year', 'Month'], axis =1)


#Export into CSV

data.to_csv("ValueInc_Cleaned.csv", index = False)
