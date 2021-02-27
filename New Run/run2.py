import pandas as pd
votes = ['Votes/H106_votes.csv','Votes/H107_votes.csv','Votes/H108_votes.csv','Votes/HS109_votes.csv','Votes/HS110_votes.csv','Votes/HS111_votes.csv'
         ,'Votes/HS112_votes.csv','Votes/HS113_votes.csv','Votes/HS114_votes.csv','Votes/H115_votes.csv']
members = ['Votes/H106_members.csv','Votes/H107_members.csv','Votes/H108_members.csv','Votes/H109_members.csv','Votes/H110_members.csv'
           ,'Votes/H111_members.csv','Votes/H112_members.csv','Votes/H113_members.csv','Votes/H114_members.csv','Votes/H115_members.csv']
bills = 'bill_list_best.csv'
runner = -1
w = open('member_list_best1.csv', 'w')
w.write('CongressNum,Name,Party,State,District,allAverage,partisanAverage,billAverage,procedureAverage,resolutionAverage \n')
bill_spot = 0
while runner < len(members) - 1:
    runner += 1
    df = pd.read_csv(members[runner])
    party = df.party_code
    icpsr1 = df.icpsr
    name = df.bioname
    state = df.state_abbrev
    district = df.district_code
    df = pd.read_csv(votes[runner])
    icpsr = df.icpsr
    votecode = df.cast_code
    roll=df.rollnumber
    df = pd.read_csv(bills, encoding='windows-1252')
    roll1 = df.rollnumber
    dem = df.dem
    rep = df.rep
    type= df.vote_type
    code = df.bill_code
    partisan = df.if_partisan
    averages = []
    averages_partisan= []
    j = 0
    x = -1
    while x+1 < len(icpsr1):
        x = x+1
        n = 0
        m = 0
        n1 = 0
        m1 = 0
        nres = 0
        mres = 0
        npassage = 0
        mpassage = 0
        nprocedure = 0
        mprocedure = 0
        j = j+1
        if party[x]==100:
            part = dem
            i = -1
            while i + 1 < len(votecode):
                i = i + 1
                if icpsr[i] == icpsr1[x]:
                    if int(votecode[i]) == int(dem[int(roll[i]) + bill_spot- 1]):
                        n = n + 1
                        m = m + 1
                        if partisan[int(roll[i]) - 1] == 1:
                            n1 += 1
                            m1 += 1
                        l = str(code[int(roll[i])+ bill_spot - 1]).lower()
                        k = str(type[int(roll[i])+ bill_spot - 1]).lower()
                        if 'res' in l and 'j' not in l:
                            nres += 1
                            mres += 1
                        elif 'pass' in k:
                            npassage += 1
                            mpassage += 1
                        else:
                            nprocedure += 1
                            mprocedure += 1
                    elif votecode[i] == 1:
                        m = m + 1
                        if partisan[int(roll[i])+ bill_spot - 1] == 1:
                            m1 += 1
                        l = str(code[int(roll[i])+ bill_spot - 1]).lower()
                        k = str(type[int(roll[i])+ bill_spot - 1]).lower()
                        if 'res' in l and 'j' not in l:
                            mres += 1
                        elif 'pass' in k:
                            mpassage += 1
                        else:
                            mprocedure += 1
            if m > 0:
                average = n / m
                if m1 > 0:
                    average1 = n1 / m1
                else:
                    average1 = 0
                if mpassage > 0:
                    average2 = npassage / mpassage
                else:
                    average2 = 0
                if mprocedure > 0:
                    average3 = nprocedure / mprocedure
                else:
                    average3 = 0
                if mres > 0:
                    average4 = nres / mres
                else:
                    average4 = 0
            else:
                average = 0
                average1 = 0
                average2 = 0
                average3 = 0
                average4 = 0
        else:
            part = rep
            i = -1
            while i + 1 < len(votecode):
                i = i + 1
                if icpsr[i] == icpsr1[x]:
                    if int(votecode[i]) == int(rep[int(roll[i])+ bill_spot - 1]):
                        n = n + 1
                        m = m + 1
                        if partisan[int(roll[i])+ bill_spot - 1] == 1:
                            n1 += 1
                            m1 += 1
                        l = str(code[int(roll[i])+ bill_spot - 1]).lower()
                        k = str(type[int(roll[i])+ bill_spot - 1]).lower()
                        if 'res' in l and 'j' not in l:
                            nres += 1
                            mres += 1
                        elif 'pass' in k:
                            npassage += 1
                            mpassage += 1
                        else:
                            nprocedure += 1
                            mprocedure += 1

                    elif votecode[i] == 1:
                        m = m + 1
                        if partisan[int(roll[i]) - 1] == 1:
                            m1 += 1
                        l = str(code[int(roll[i])+ bill_spot - 1]).lower()
                        k = str(type[int(roll[i])+ bill_spot - 1]).lower()
                        if 'res' in l and 'j' not in l:
                            mres += 1
                        elif 'pass' in k:
                            mpassage += 1
                        else:
                            mprocedure += 1
            if m > 0:
                average = n / m
                if m1 > 0:
                    average1 = n1 / m1
                else:
                    average1 = 0
                if mpassage > 0:
                    average2 = npassage / mpassage
                else:
                    average2 = 0
                if mprocedure > 0:
                    average3 = nprocedure / mprocedure
                else:
                    average3 = 0
                if mres > 0:
                    average4 = nres / mres
                else:
                    average4 = 0
            else:
                average = 0
                average1 = 0
                average2 = 0
                average3 = 0
                average4 = 0
        congress = 106 + runner
        print(name[x] + ', ' + str(state[x]) + ', ' + str(district[x]) + ', ' + str(average) + ', ' + str(average1) + ', ' + str(average2) + ', ' + str(average3)+ ', ' + str(average4) )
        w = open('member_list_best1.csv', 'a')
        w.write(str(congress) + ',' + name[x].replace(',', ';') + ',' + str(party[x]) + ',' + str(state[x]) + ',' + str(district[x]) + ',' + str(average) + ',' +
                str(average1) + ',' + str(average2) + ', ' + str(average3) + ',' + str(average4) + '\n')
        averages.append(average)
        averages_partisan.append(average1)
    bill_spot = int(roll[len(roll)-1])-1