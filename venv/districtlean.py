import pandas as pd

lean = "Daily Kos Elections 2008 & 2012 presidential election results for congressional districts used in 2012 & 2014 elections - Results.csv"
avg_margin = "2012_avg_margin.csv"

df = pd.read_csv(lean)
obama8=df.Obama12
mccain=df.McCain
obama12=df.Obama12
romney=df.Romney
district2=df.CD

df = pd.read_csv(avg_margin)
state=df.State
district=df.District


j=-1
while j+1<len(district):
     n=-1
     j=j+1
     while n+1<len(district2):
         n=n+1
         state1=str(state[j])
         district1=str(district[j])
         district3=str(district2[n])

         if (state1 in district3 and district1 in district3) or (district[j]==0 and state1 in district3):

             first=obama12[n]-romney[n]
             second=obama8[n]-mccain[n]
             #third=gore[n]-bush0[n]
             print("{} {} {} {}".format(state[j], district[j], first,second))
             n=len(district2)

