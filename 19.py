a = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55.0, 'item5': 24}
b=0
d={}
for i,j in a.items():
    if type(j)==float:
        d[i]=j
print(d)











# item4 55                                                                                                      
# item1 45.5                                                                                                    
# item3 41.3 