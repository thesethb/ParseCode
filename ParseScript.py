# importing csv module
import csv

import pandas as pd


# csv file name
members = "H106_members.csv"
votes = "H106_votes.csv"
Rep=14421
Dem=15125
Pelosi1 = "Pelosi114.csv"
McCarthy1 ="mccarthy2.csv"
Write="writeover.csv"
# initializing the titles and rows list
fields = []
rows = []
# reading csv file
averages = []
votercodes = []
df = pd.read_csv(members)
numbers = df.icpsr
party = df.party_code
j = 0
x = -1
i=-1
df = pd.read_csv(votes)
voter = df.icpsr
votecode = df.cast_code
billnum = df.rollnumber
#df = pd.read_csv(Pelosi1)
Pelosi = []
#df = pd.read_csv(McCarthy1)
McCarthy = []
while i + 1 < len(votecode):
    i = i + 1
    if voter[i] == Dem:
        Pelosi.append(votecode[i])
k=-1
while k + 1 < len(votecode):
    k = k + 1
    if voter[k] == Rep:
       McCarthy.append(votecode[k])
while x+1 < len(numbers):
    x = x+1
    n = 0
    m = 0
    j = j+1
    if party[x]==100:
        leader = Pelosi
    else:
        leader = McCarthy


    i = -1
    while i+1 < len(votecode):
        i=i+1
        if voter[i] == numbers[x]:
            if int(votecode[i])== int(leader[int(billnum[i])-1]):
                n=n+1
                m=m+1
            elif votecode[i] != 9:
                m=m+1
    if m > 0:
        average = n / m
    else:
         average = 0
    print(average)
    votercodes.append(numbers[x])
    averages.append(average)
city = pd.DataFrame(averages)
city.to_csv(Write)