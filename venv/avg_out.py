import pandas as pd
total1 = 'bigdata_no0.csv'
df = pd.read_csv(total1)
avg_def = df.Avg_Def
year = df.Year1
n = 0
year1 = year[0]
while n < len(year):
    m = n
    total = 0
    while m < len(year) and year[m] == year1:
        total += avg_def[m]
        m += 1
    avg = total / (m-n)
    while n < len(year) and year[n] == year1:
        print(str(float(avg_def[n]-avg)))
        n += 1
    if n < len(year):
        year1 = year[n]
