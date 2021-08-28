a={'a':'shahna','b':'shireen','c':'navya','d':'sandhya','e':'shahna','f':'shireen','g':'navya','h':'sandhya','i':'shahna','j':'shireen','k':'navya','l':'sandhya'}
b=list(a.values())
d={}
for k in b:
    i=0
    while i<len(b):
        j=0
        c=0
        while j<len(b):
            if b[i]==b[j]:
                c=c+1
            j=j+1
        i=i+1
    d[k]=c
print(d)
print('_____________________________________________________________________')