d={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
v=list(d.values())
i=0
while i<len(v):
    j=0
    while j<len(v[i]):
        if v[i][j]==v[i][4]:
            print(v[i][j])
        j=j+1
    i=i+1
#  15
# 25
# 35






# 1,2,6,24,120,...this process is going like 1*2=2.2*3=6.6*4=24.24*5=
i=1
j=1

