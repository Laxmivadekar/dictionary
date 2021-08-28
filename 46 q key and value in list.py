a=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d={}
for i in a:
    b=[]
    k=i[0]
    for j in a:
        if j[0]==k:
            b.append(j[1])
        d[k]=b
print(d)
print('___________________')
i=0
d={}
while i<len(a):
    b=[]
    j=0
    while j<len(a):
        if a[i][0]==a[j][0]:
            b.append(a[j][1])
        j=j+1
    d.update({a[i][0]:b})
    i=i+1
print(d)







# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}