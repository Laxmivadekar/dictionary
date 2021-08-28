a={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
b=list(a.values())
# d={}
# main_list=[]
# for k in a:
#     i=0
#     c=[]
#     while i<len(b):
#         j=0
#         while j<len(b[i]):
#             c.append(b[i][j])
#             d[k]=c
#             j=j+1
#         i=i+1
#         main_list.append(d)
# print(main_list)
# A key-value list pairings of the said dictionary:
# [{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]

for i in a:
    b=a[i]
    a[i]=b[0]
print(a)