import pandas as pd
votes = ['Votes/H106_votes.csv','Votes/H107_votes.csv','Votes/H108_votes.csv','Votes/HS109_votes.csv','Votes/HS110_votes.csv','Votes/HS111_votes.csv'
         ,'Votes/HS112_votes.csv','Votes/HS113_votes.csv','Votes/HS114_votes.csv','Votes/H115_votes.csv']
members = ['Votes/H106_members.csv','Votes/H107_members.csv','Votes/H108_members.csv','Votes/H109_members.csv','Votes/H110_members.csv'
           ,'Votes/H111_members.csv','Votes/H112_members.csv','Votes/H113_members.csv','Votes/H114_members.csv','Votes/H115_members.csv']
bills = ['Votes/H106_rollcalls.csv','Votes/H107_rollcalls.csv','Votes/H108_rollcalls.csv','Votes/H109_rollcalls.csv','Votes/H110_rollcalls.csv'
           ,'Votes/H111_rollcalls.csv','Votes/H112_rollcalls.csv','Votes/H113_rollcalls.csv','Votes/H114_rollcalls.csv','Votes/H115_rollcalls.csv']
z = 0
while z < len(members):
    #Part1: Assigning Party
    df = pd.read_csv(votes[z])
    icpsr = df.icpsr
    df = pd.read_csv(members[z])
    party = df.party_code
    icpsr1 = df.icpsr
    partylist = [[]]
    for item in icpsr:
        n = 0
        while n < len(icpsr1):
            if item == icpsr1[n]:
                partylist[0].append(party[n])
            n += 1
    print(partylist)
    #Part 2: Calculating averages, adding every partisan bill to billlist with info of which party voted each way
    n = 0
    df = pd.read_csv(votes[z])
    billnum = df.rollnumber
    cast_code = df.cast_code
    num = billnum[0]
    billlist = []
    while n < len(icpsr):
        num = billnum[n]
        dem_avg = 0
        dem_avg1 = 0
        rep_avg = 0
        rep_avg1 = 0
        while n < len(icpsr) and billnum[n] == num:
            if partylist[0][n] == 100:
                if cast_code[n] == 6:
                    dem_avg += 1
                    dem_avg1 += 1
                if cast_code[n] == 1:
                    dem_avg1 += 1
            if partylist[0][n] == 200:
                if cast_code[n] == 6:
                    rep_avg += 1
                    rep_avg1 += 1
                if cast_code[n] == 1:
                    rep_avg1 += 1
            n += 1
        dem_avg = dem_avg/dem_avg1
        rep_avg = rep_avg/rep_avg1
        if dem_avg > .5 and rep_avg < .5:
            billlist.append([billnum[n-1],6,1,1])
            print('affirmative')
        elif dem_avg < .5 and rep_avg > .5:
            billlist.append([billnum[n-1],1,6,1])
            print('hi')
        elif dem_avg > .5:
            billlist.append([billnum[n - 1], 6, 6, 0])
        else:
            billlist.append([billnum[n - 1], 1, 1, 0])
    #Part3, attaching info to bills and exporting to spreadsheet
    df = pd.read_csv(bills[z])
    con = df.congress
    billnum1 = df.rollnumber
    info = [df['bill_number'].values.tolist(), df['vote_result'].values.tolist(), df['vote_desc'].values.tolist(), df['vote_question'].values.tolist(), df['dtl_desc'].values.tolist()]
    w = open('bill_list_best.csv', 'a')
    for bill in billlist:
        n = 0
        while n < len(billnum1):
            if bill[0] == billnum1[n]:
                string1 = str(info[4][n])
                string2 = str(info[3][n])
                string3 = str(info[2][n])
                print(str(bill[0]) + ', ' + str(bill[1]) + ', ' + str(bill[2]) + ', ' + str(bill[3]) + ', '+ str(info[0][n]) + ', ' +  str(info[1][n]) + ', ' +  str(info[2][n]).replace(',', ';') + ', ' +  str(info[3][n]).replace(',', ';') + ', ' +  str(info[4][n]).replace(',', ';'))
                s = str(106 + z) + ', ' + str(bill[0]) + ', ' + str(bill[1]) + ', ' + str(bill[2]) + ', ' + str(bill[3]) + ', '+ str(info[0][n]) + ', ' +  str(info[1][n]) + ', ' +  string3.replace(',', ';') + ', ' +  string2.replace(',', ';') + ', ' +  string1.replace(',', ';') + '\n'
                w.write(s)
            n += 1
    z += 1