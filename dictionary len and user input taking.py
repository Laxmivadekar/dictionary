def f():
    user1=int(input('enter the length'))
    a=[]
    b=[]
    i=0
    while i<user1:
        n1=int(input('enter the number'))
        n2=int(input('enter a number'))
        a.append(n1)
        b.append(n2)
        c=[]
        j=0
        while j<=i:
            c.append(a[j]+b[j])
            j=j+1
        i=i+1
    print(c)
f()
