# importing csv module
import csv

import pandas as pd


# csv file name
members = "HS114_members.csv"
votes = "HS114_votes.csv"
Rep=20703
Dem=15448
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
n = 0
m = 0
while(m < len(billnum)):
    n=n+1
    r=0
    j=0
    x=0
    y=0
    w=0
    f=0
    while(billnum[m] == n):
        z=0
        while(z < len(party)):
            if(numbers[z] == voter[m]):
                if(party[z] == 100):
                    if(Pelosi[n - 1] == votecode[m]):
                        r = r + 1
                        x=x+1
                    elif(Pelosi[n - 1] != votecode[m] and votecode[m] != 9):
                        j = j + 1
                        r = r + 1
                        y=y+1
                        x=x+1
                    z == len(party)
                if (party[z] == 200):
                    if (McCarthy[n - 1] == votecode[m]):
                        r = r + 1
                        w=w+1
                    elif (McCarthy[n - 1] != votecode[m] and votecode[m] != 9):
                        j = j + 1
                        r = r + 1
                        f=f+1
                        w=w+1
                    z == len(party)
            z = z + 1
        m = m + 1
        if(m >= len(billnum)):
            break
    percent = 0
    dempercent = 0
    reppercent = 0
    if (x != 0):
        dempercent = y / x
    if (w != 0):
        reppercent = f / w
    if(r != 0):
        percent = j/r
    print(n, percent, dempercent, reppercent)

city = pd.DataFrame(averages)
city.to_csv(Write)