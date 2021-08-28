a={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
b=[]
for v in a.values():
    b.append(v)
d={}
k=0
for i in a:
    b1=[]
    j=0
    while j<len(b[k]):
        if b[k][j]%2==0:
            b1.append(b[k][j])
        j=j+1
    d[i]=b1
    k=k+1
    
print(d)
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
print('___________________________________________________________')
a= {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
b=[]
for v in a.values():
    b.append(v)
d={}
k=0
for i in a:
    b1=[]
    j=0
    while j<len(b[k]):
        if b[k][j]%2==0:
            b1.append(b[k][j])
        j=j+1
    d[i]=b1
    k=k+1
    
print(d)
print('______________________________________________________')
a={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
d={}
for i,j in a.items():
    b=[]
    for k in j:
        if k%2==0:
            b.append(k)
            d[i]=b
            print(b)

# Filter even numbers from said dictionary values:
# {'V': [], 'VI': [], 'VII': [2]}