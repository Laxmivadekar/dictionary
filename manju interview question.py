d={'m':[3,1,2],'s':[5,2,1],'k':[10,8,7]}
b=list(d.values())
e={}
for k in d:
    v=d[k]
    i=0
    while i<len(v):
        j=0
        while j<len(v)-1:
            if b[i][j]>b[i][j+1]:
                b[i][j],b[i][j+1]=b[i][j+1],b[i][j]
                # temp=b[i][j]
                # b[i][j]=b[i][j+1]
                # b[i][j+1]=temp
            j=j+1
        i=i+1
    d[k]=v
        # e[k]=c
    e[k]=c
print(e)