a=[{'v':'soo1'},{'v':'soo2'},{'vi':'soo1'},{'vi':'soo5'},{'vii':'soo5'},{'v':'soo9'},{'vii':'soo7'}]
b=[]
for i in a:
    for j in i.values():
        if j not in b:
            b.append(j)
            
print(set(b))


print('______________________________')
# d={}
# for i in a:
#     for j in i.values():
#         if j not in d:
#             d=j
#             print(d)