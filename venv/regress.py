import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
total = 'bigdata.csv'
total1 = 'bigdata_no0.csv'
new = 'yearData.csv'
#df = pd.read_csv(total)
df = pd.read_csv(total1)
year = df.Year[0]
n = -1
Lean, Minority, Nat_Margin, Fresh, Avg_Def_Adj, Margin, Year, Calculated_C6 =[],[],[],[],[],[],[],[]
m = 0

while n < len(df.Lean) - 1:
    n += 1
    if df.Year[n] != year or n == len(df.Lean) - 1:
        #X = df.Lean[m:n] , df.Minority[m:n], df.Nat_Margin[m:n], df.Fresh[m:n], df.Avg_Def[m:n]]
        X = df[["Avg_Def","Lean","Fresh"]][m:n]
        X = sm.add_constant(X)
        y = df.Margin[m:n]
        model = sm.OLS(y, X).fit()
        predictions = model.predict(X)
        x = str(model.summary())
        f = open(str(year) + str(df.Party[n-1]) + '.txt','w')
        f.write(x)
        m = n
        #Lean, Minority, Nat_Margin, Fresh, Avg_Def, Margin, Year, Calculated_C6 = [], [], [], [], [], [], [], []
        year = df.Year[n]
    #Lean.append(df.Lean[n]), Minority.append(df.Minority[n]), Nat_Margin.append(df.Nat_Margin[n]), Fresh.append(
        #df.Fresh[n]), Avg_Def.append(df.Avg_Def[n]), Margin.append(df.Margin[n]), Year.append(df.Year[n]), Calculated_C6.append(
        #df.Calculated_C6[n])

#df = pd.read_csv(new)
X = df[["Lean", "Minority", "Nat_Margin", "Fresh", "Avg_Def","Midterm","Party", "Year1",'Has_Pres',"DefxParty","DefxLean","DefxMin",
        "DefxNat_Margin","DefxYear1","DefxFresh","DefxMid",'DefxHas_Pres']]
#X1 = df[["Lean", "Minority", "Nat_Margin", "Fresh", "Year1","Midterm","Party"]]
y = df["Margin"]
#y1 = df.Calculated_C6
#X = sm.add_constant(X)
#X1=df[["Year1","Has_Pres", "Midterm","Minority","Party",'MinxParty']]
#y1 = df.C6
X = sm.add_constant(X)
model = sm.OLS(y,X).fit()
predictions = model.predict(X)
x = str(model.summary())
f = open('InteractiveReg.txt','w')
f.write(x)

#Note: excluded from sample are: uncontested races(no major pary competitor with >10000 votes) and members who had not voted against their party once(because they only had a small amount of votes cast)

