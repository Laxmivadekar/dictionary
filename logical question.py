a={'math':[88,89,90],'physics':[92,94,89],'chemistry':[90,87,93]}
b=list(a.values())
print(b)
d=[]    
i=0
while i<len(b):
    j=0
    c=[]
    while j<len(b[i]):
        if i%2==0:
            c.append(b[i][j]+1)
        else:
            c.append(b[i][j]-2)
        j=j+1
        # d[k]=c
    i=i+1
    d.append(c)
print(d)
f=[]
for k in a:
    f.append(k)
i=0
e={}
while i<len(d):
    e[f[i]]=d[i]
    i=i+1
print(e)
print('____________________________________________________')
a={'math':[88,89,90],'physics':[92,94,89],'chemistry':[90,87,93]}
b=list(a.values())
e=[]
for k in a:
    e.append(k)
main_dict={}   
i=0
while i<len(b):
    j=0
    c=[]
    while j<len(b[i]):
        if i%2==0:
            c.append(b[i][j]+1)
        else:
            c.append(b[i][j]-2)
        j=j+1
    main_dict[e[i]]=c
    i=i+1
print(main_dict)



# new_func(b)
#         d[k]=c
# print(d)


