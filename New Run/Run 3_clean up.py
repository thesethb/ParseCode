import pandas as pd
df = pd.read_csv('member_election_list_best.csv')
name = df.name
congress = df.congress
n = 0
name1 = ''
congress1 = ''
while n < len(name):
    if name[n] == name1 and congress[n] == congress1:
        print(name[n] + ' ' + str(congress[n]) + ' ' + str(n))
    name1 = name[n]
    congress1 = congress[n]
    n += 1