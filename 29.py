d={'m':[3,1,2],'s':[5,2,1],'k':[10,8,7]}
b=list(d.values())
# print(b)
a={}
for k in d:
    i=0
    c=[]
    while i<len(b):
        j=0
        while j<len(b[i])-1:
            if b[i][j]<b[i][j+1]:
                b[i][j],b[i][j+1]=b[i][j+1],b[i][j]
            j=j+1
        c.append(b)
        i=i+1
    a[k]=c
print(a)

a=[3,1,2],[5,2,1],[10,8,7]