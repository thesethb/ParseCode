import pandas as pd
votes = ['Votes/S116_votes.csv','Votes/S115_votes.csv','Votes/S114_votes.csv','Votes/S113_votes.csv','Votes/S112_votes.csv','Votes/S111_votes.csv']
members = ['Votes/S116_members.csv','Votes/S115_members.csv','Votes/S114_members.csv','Votes/S113_members.csv','Votes/S112_members.csv','Votes/S111_members.csv']
bills = ['Votes/S116_rollcalls.csv','Votes/S115_rollcalls.csv','Votes/S114_rollcalls.csv','Votes/S113_rollcalls.csv','Votes/S112_rollcalls.csv','Votes/S111_rollcalls.csv']
majority = ['rep','rep','rep','dem','dem','dem']
w = open('bill_list_best.csv', 'w')
w.write('Congress,Majority, votenum, min_vote,maj_vote,if_partisan,case_num,bill_num,vote_name, bill_name,more,more1 \n')
w.close()
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
                if cast_code[n] == 1:
                    dem_avg += 1
                    dem_avg1 += 1
                if cast_code[n] == 6:
                    dem_avg1 += 1
            if partylist[0][n] == 200:
                if cast_code[n] == 1:
                    rep_avg += 1
                    rep_avg1 += 1
                if cast_code[n] == 6:
                    rep_avg1 += 1
            n += 1
        dem_avg2 = dem_avg/dem_avg1
        rep_avg2 = rep_avg/rep_avg1
        if majority[z] == 'rep':
            maj_avg2,maj_avg,maj_avg1 = rep_avg2,rep_avg,rep_avg1
            min_avg2, min_avg, min_avg1 = dem_avg2, dem_avg, dem_avg1
        else:
            maj_avg2, maj_avg, maj_avg1 = dem_avg2, dem_avg, dem_avg1
            min_avg2, min_avg, min_avg1 = rep_avg2, rep_avg, rep_avg1
        case_num = 0
        if (maj_avg + min_avg > 60 and min_avg2 < .5):
            case_num = 2
        elif maj_avg2 > .5 and min_avg2 > .5:
            case_num = 1
        elif maj_avg + min_avg > 50 and maj_avg <= (maj_avg + min_avg) / 2:
            case_num = 3
        elif maj_avg + min_avg < (maj_avg + min_avg) / 2 and maj_avg2 > .5:
            case_num = 4
        if min_avg2 > .5 and maj_avg2 < .5:
            billlist.append([billnum[n-1],1,6,1,case_num])
            print('affirmative')
        elif min_avg2 < .5 and maj_avg2 > .5:
            billlist.append([billnum[n-1],6,1,1,case_num])
            print('hi')
        elif min_avg2 < .5:
            billlist.append([billnum[n - 1], 6, 6, 0,case_num])
        else:
            billlist.append([billnum[n - 1], 1, 1, 0,case_num])
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
                print(str(bill[4]))
                s = str(116 - z) + ', ' + str(majority[z]) + ', ' + str(bill[0]) + ', ' + str(bill[1]) + ', ' + str(bill[2]) + ', ' + str(bill[3]) +',' + str(bill[4]) + ', '+ str(info[0][n]) + ', ' +  str(info[1][n]) + ', ' +  string3.replace(',', ';') + ', ' +  string2.replace(',', ';') + ', ' +  string1.replace(',', ';')  + '\n'
                w.write(s)
            n += 1
    z += 1