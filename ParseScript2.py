import csv
import pandas as pd
def parseCongress( members , votes, Dem, Rep, Write):

    Pelosi = []
    McCarthy = []

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
    i = -1
    df = pd.read_csv(votes)
    voter = df.icpsr
    votecode = df.cast_code
    billnum = df.rollnumber
    while i + 1 < len(votecode):
        i = i + 1
        if voter[i] == Dem:
            Pelosi.append(votecode[i])
    k = -1
    while k + 1 < len(votecode):
        k = k + 1
        if voter[k] == Rep:
            McCarthy.append(votecode[k])
    while x + 1 < 5:  # len(numbers):
        x = x + 1
        n = 0
        m = 0
        j = j + 1
        if party[x] == 100:
            leader = Pelosi
        else:
            leader = McCarthy

        i = -1
        while i + 1 < len(votecode):
            i = i + 1
            if voter[i] == numbers[x]:
                if votecode[i] == leader[billnum[i] - 1]:
                    n = n + 1
                    m = m + 1
                elif votecode[i] != 9:
                    m = m + 1
        if m > 0:
            average = n / m
        else:
            average = 0
        print(average)
        votercodes.append(numbers[x])
        averages.append(average)
    city = pd.DataFrame(averages)
    city.to_csv(Write)
if_name_=="main":
    parseCongress("H113_members.csv","HS113_votes.csv",15448,20703,"113.csv")
    parseCongress("H112_members.csv","HS113votes.csv",15448,20144,"112.csv")