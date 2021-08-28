a=input('enter the name')
i=0
d={}
while i<len(a):
    d[a[i]]=a
    i=i+1
print(d)
print('________________________________')


a=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d={}
b=[]
for i,j in a:
    d.setdefault(i,[]).append(j)
print(d)







# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
