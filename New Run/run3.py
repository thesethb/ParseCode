import pandas as pd
import io
members = "member_list_best.csv"
rep = "repdata.csv"
dem = "demdata.csv"
df = pd.read_csv(rep)
repnames = df.candidate
reptotalvotes = df.totalvotes
repcandvotes = df.candidatevotes
repstate=df.state_po
repdistrict=df.district
repyear=df.year


df = pd.read_csv(dem)
demnames = df.candidate
demtotalvotes = df.totalvotes
demcandvotes = df.candidatevotes
demstate=df.state_po
demdistrict=df.district
demyear=df.year
w = open('member_election_list.csv', 'w')
w.write('congress,year,name,party,state,district,margin,allAverage,partisanAverage,billAverage,procedureAverage,resolutionAverage\n')
w.close()
df = pd.read_csv(members)
membersnames = df.Name
membersstate=df.State
membersdistrict=df.District
avg1 = df.allAverage
avg2 = df.partisanAverage
avg3 = df.billAverage
avg4 = df.procedureAverage
avg5 = df.resolutionAverage
party = df.Party
congress = df.CongressNum
n=4300
while n - 1 >= 0:
     year = 2000
     j=-1
     n=n-1
     while j+1<len(membersnames) and demyear[n]>year:
         j = j + 1
         year = (congress[j] - 106)*2 + 2000
     while j+1<len(membersnames) and demyear[n]>=year:
         j=j+1
         name = membersnames[j].replace(' ', '')
         name = name.lower()
         name = name.split(';')
         numeroUno = name[1][0]
         last = name[0][0:3]
         demname = demnames[n].lower()
         state = membersstate[j].replace(' ', '')
         year = (congress[j] - 106) * 2 + 2000
         if (last in demname and numeroUno == demname[0] and demstate[n]==state and party[j] == 100)or(last in demname and numeroUno == demname[0] and demstate[n]==membersstate[j] and 0 ==demdistrict[n] ):
            print('a')
            m=n+200
            while(m-1 > 0 and repyear[m-1]<=year):
                m=m-1

                if(repyear[m]==year and demstate[n]==repstate[m] and demdistrict[n]==repdistrict[m] and repcandvotes[m]>10000):
                    marginvotes=demcandvotes[n]-repcandvotes[m]
                    margin=100*marginvotes/demtotalvotes[n]
                    #congress, year, name, party, state, district, allAverage, partisanAverage, billAverage, procedureAverage, resolutionAverage
                    #print("{},{},{},{},{},{},{},{},{}".format(year, congress[j], name[j], party[j], demstate[n],demdistrict[n],margin,avg1[j],avg2[j],avg3[j],avg4[j],avg5[j]))
                    print(n)
                    print(j)
                    print(last)
                    print(numeroUno)
                    printed = str(year) + ',' + str(congress[j]) + ',' + str(membersnames[j]) + ',' +  str(party[j]) + ',' +  str(demstate[n])  + ',' + str(demdistrict[n]) + ',' +  str(margin) + ',' +  str(avg1[j]) + ',' +  str(avg2[j]) + ',' + str(avg3[j]) + ',' +  str(avg4[j]) + ',' +  str(avg5[j]) +'\n'
                    print(printed)
                    with io.open('member_election_list.csv', "a", encoding="utf-8") as f:
                        f.write(printed)

print('elephant')
n=4300
while n - 1 >= 0:
     year = 2000
     j=-1
     n=n-1
     while j+1<len(membersnames) and repyear[n]>year:
         j = j + 1
         year = (congress[j] - 106)*2 + 2000
     while j+1<len(membersnames) and repyear[n]>=year:
         j=j+1
         name = membersnames[j].replace(' ', '')
         name = name.lower()
         name = name.split(';')
         numeroUno = name[1][0]
         last = name[0][0:3]
         repname = repnames[n].lower()
         state = membersstate[j].replace(' ', '')
         year = (congress[j] - 106) * 2 + 2000
         if last in repname and numeroUno == repname[0] and repstate[n]==state and party[j] == 200:
            print('a')
            m=n+200
            while(m-1 > 0 and demyear[m-1]<=year):
                m=m-1

                if(demyear[m]==year and repstate[n]==demstate[m] and repdistrict[n]==demdistrict[m] and demcandvotes[m]>10000):
                    marginvotes=repcandvotes[n]-demcandvotes[m]
                    margin=100*marginvotes/reptotalvotes[n]
                    #congress, year, name, party, state, district, allAverage, partisanAverage, billAverage, procedureAverage, resolutionAverage
                    #print("{},{},{},{},{},{},{},{},{}".format(year, congress[j], name[j], party[j], demstate[n],demdistrict[n],margin,avg1[j],avg2[j],avg3[j],avg4[j],avg5[j]))
                    print(n)
                    print(j)
                    print(last)
                    print(numeroUno)
                    printed = str(year) + ',' + str(congress[j]) + ',' + str(membersnames[j]) + ',' +  str(party[j]) + ',' +  str(repstate[n])  + ',' + str(repdistrict[n]) + ',' +  str(margin) + ',' +  str(avg1[j]) + ',' +  str(avg2[j]) + ',' + str(avg3[j]) + ',' +  str(avg4[j]) + ',' +  str(avg5[j]) +'\n'
                    print(printed)
                    with io.open('member_election_list.csv', "a", encoding="utf-8") as f:
                        f.write(printed)