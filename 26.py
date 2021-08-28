a={'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
b=list(a.values())
d={}
for k in b:
    i=0
    while i<len(b):
        j=0
        c=0
        while j<len(b):
            if k==b[j]:
                c=c+1
            d[k]=c
            j=j+1
        i=i+1
print(d)
print('_________________________________________________')
a={'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
b=list(a.values())
d={}
for k in b:   
    j=0
    c=0
    while j<len(b):
        if k==b[j]:
            c=c+1
        d[k]=c
        j=j+1
print(d)
print('_________________________________________________')


# Count the frequency of the said dictionary:
# Counter({10: 2, 40: 2, 20: 2, 70: 1, 80: 1})
# Click me to see the sample solutionb=


b=[]
d={}
for v in a.values():
    if v not in b:
        b.append(v)
i=0
while i<len(b):
    c=0
    for j in a:
        if a[j]==b[i]:
            c=c+1
    d[b[i]]=c
    i=i+1
print(d)
print('______________________________________________________________')
b=[]
d={}
for v in a.values():
    # if v not in b:
    b.append(v)
    c=0
    for j in a:
        if v==a[j]:
            c=c+1
        d[v]=c
print(d)


