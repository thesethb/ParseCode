import pandas as pd

lean = "2006-10.csv"
avg_margin = "2002_avg_margin.csv"

df = pd.read_csv(lean)

obama = df.Obama
mccain=df.McCain
kerry=df.Kerry
bush4=df.Bush4
gore=df.Gore
bush0=df.Bush0
district2=df.CD
state2=df.State

df = pd.read_csv(avg_margin)
state=df.State
district=df.District


j=-1
while j+1<len(district):
     n=-1
     j=j+1
     while n+1<len(state2):
         n=n+1
         state1=str(state[j])
         district1=str(district[j])
         #district2=str(state_district[n])
         if (state1 == state2[n] and district1 == district2[n]) or (district[j]==0 and state1 ==state2[n]):
             first=obama[n]-mccain[n]
             second=kerry[n]-bush4[n]
             third=gore[n]-bush0[n]
             print("{} {} {} {}".format(state[j], district[j], second,third))
             n=len(state2)

