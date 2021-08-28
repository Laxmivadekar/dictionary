a={'h':'red','m':'red','s':'green','k':'black','g':'green'}
d=''
for i in a:
    for j in a:
        if i==j and i!='k':
            d=i           
            print(d)