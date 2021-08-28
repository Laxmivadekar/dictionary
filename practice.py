a=input('enter a name')
b=''
i=0
while i<=1:
    b=b+a[i]
    i=i+1
c=''+b
i=2
while i>=1:
    c=c+a[-i]
    i=i-1
print(c)