import pandas as pd
df = pd.read_csv('Book1.csv')
exp = df.Expiremental
the = df.Theoretical
f = df.Frequency
er = df.Error
n = 0
while n < len(exp):
    print('{Around['+str(f[n])+','+str(er[n]) + '], Around['+str(exp[n])+',' + str(er[n]) + ']},')
    n+=1
print('\n')
n = 0
while n < len(exp):
    print('{'+str(f[n])+','+str(the[n])+'},')
    n+=1
