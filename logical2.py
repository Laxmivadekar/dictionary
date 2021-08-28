a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
d={}
for key,values in a.items():
    d[values]=key
print(d)
print('_____________________________________________')
a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
b=list(a.keys())
c=list(a.values())
d={}
i=0
while i<len(b):
    e=c[i]
    d[e]=b[i]
    i=i+1
print(d)
print('________________________________________')
# dic={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# a=[]
# for i in dic:
#     a.append(i)
# b=[]
# for j in dic.values():
#     b.append(j)
# d={}
# for k in b:
#     for v in a:
#         d[k]=v
# print(d)
print('_____________________________________________________________________________')
a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
b=list(a.keys())
c=list(a.values())
d={}
for i in b:
    e=c[i]
    d[e]=b[i]
print(d)