a={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
b=[]
for i in a.values():
    b.append(i)
# i=0
# b1=[]
# while i<4:
#     d={}
#     j=0
#     for k in a:
#         d[k]=b[j][i]
#         j=j+1
#     b1.append(d)
#     i=i+1
# print(b1)

b=list(a.keys())
c=list(a.values())
print(b)
print(c)
i=0
d=[]
while i<len(b):
    j=0
    e={}
    while j<len(c):
        e[i][j]=c[j][i]
        j=j+1
    d.append(d)
    i=i+1
print(d)


# Split said dictionary of lists into list of dictionaries:
# # [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
