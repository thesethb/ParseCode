import pandas as pd

members = "H107_members.csv"
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

df = pd.read_csv(members)
membersnames = df.bioname
membersstate=df.state_abbrev
membersdistrict=df.district_code
membersaverage=df.Averages
n=0
while demyear[n+1]>2001:
     j=-1
     n=n+1
     while j+1<len(membersnames) and demyear[n]==2002:
         j=j+1
         name = membersnames[j].lower()
         firstfour = name[0:4]
         demname = demnames[n].lower()
         if (firstfour in demname and demstate[n]==membersstate[j] and demdistrict[n]==membersdistrict[j])or(firstfour in demname and demstate[n]==membersstate[j] and 0 ==demdistrict[n] ):

            m=n-200
            while(repyear[m+1]>2001):
                m=m+1

                if(repyear[m]==2002 and demstate[n]==repstate[m] and demdistrict[n]==repdistrict[m] and repcandvotes[m]>10000):
                    marginvotes=demcandvotes[n]-repcandvotes[m]
                    margin=100*marginvotes/demtotalvotes[n]
                    print("{} {} 1 {} {}".format(demstate[n],demdistrict[n],membersaverage[j],margin))
            j = len(membersnames)
n=0
while repyear[n+1]>2001:
     j=-1
     n=n+1
     while j+1<len(membersnames) and repyear[n]==2002:
         j=j+1
         name=membersnames[j].lower()
         firstfour=name[0:4]
         repname=repnames[n].lower()
         if (firstfour in repname and repstate[n]==membersstate[j] and repdistrict[n]==membersdistrict[j] )or(firstfour in repname and repstate[n]==membersstate[j] and repdistrict[n]==0 ) :
            m=n-200
            while(demyear[m+1]>2001):
                m=m+1
                if(demyear[m+1]>=2002 and repstate[n]==demstate[m] and repdistrict[n]==demdistrict[m] and demcandvotes[m]>10000):
                    marginvotes=repcandvotes[n]-demcandvotes[m]
                    margin=100*marginvotes/reptotalvotes[n]
                    print("{} {} -1 {} {}".format(repstate[n],repdistrict[n],membersaverage[j],margin))
            j = len(membersnames)


