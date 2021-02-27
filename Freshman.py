import pandas as pd
years = ['H115_members.csv','HS114_members.csv','H113_members.csv','H112_members.csv','H111_members.csv'
         ,'H110_members.csv','H109_members.csv','H108_members.csv','H107_members.csv']
total = 'bigdata.csv'
df = pd.read_csv(total)
state = df.State
district = df.District
party = df.Party
defect = df.avg_defec
Year = df.Year
n = -1
j = 0
year = '2018'
while n < len(Year) - 1:
    k = 0
    n += 1
    if Year[n] != year:
        year = Year[n]
        j += 1
    df = pd.read_csv(years[j])
    if(year == '2012' or year == '2002'):
        avg = df.Average
    id = df.bioname
    state1 = df.state_abbrev
    district1 = df.district_code
    m = -1
    while m < len(id) - 1:
        m += 1
        if (state[n] == state1[m] and district[n] == district1[m]) or (state[n] == state1[m] and district[n] == 0) or ((year == '2012' or year == '2002') and state[n] == state1[m] and abs(defect[n] - 100*(1-avg[m])) < .1) :
            l = 0
            df = pd.read_csv(years[j+1])
            id1 = df.bioname
            num = 0
            while l < len(id1):
                if id1[l] == id[m]:
                    num = 1
                l += 1
            if num == 0:
                print('1' + ',' + str(year))
                k += 1
                break
    if k == 0:
        print('0' + ',' + str(year))

