# # 1+x/1!+x2/2!+x3/3!+x4/4!+.....
# import math
# j=1
# i=1
# print(i,end='')
# while j<=10:
#     print('+','x'+str(j),'/',j,'!',end=' ')
#     j=j+1

# Q54.Write a Python program to create a key-value list pairings in a given dictionary.
a={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
b=list(a.keys())
c=list(a.values())
d=list(a.items())
print(b)
print(c)
print(d)

# i=0
# d=[]
# while i<len(c):
#     if c[i]==0:
#         j=0
#         while j<len(a[i]):
#             d.append(a[i][j])
#             j=j+1
#     i=i+1
# print(d)








# A key-value list pairings of the said dictionary:
# [{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]


