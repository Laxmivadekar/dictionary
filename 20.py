a= ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
b=[1, 2, 2, 3]
i=0
c={}
while i<len(a):
    c[a[i]]={b[i]}
    i=i+1
print(c)






# while i<len(a):
#     c[a[i]]={b[i]}
#     i=i+1
# print(c)
#     c.append({b[i]})
#     i=i+1
# d={}
# for i in a:
#     d[i]=c[i]
# print(d)

# o/p:{'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}}

# a= {'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}}
# b=[]
# for i in a:
#     b.append(i)
# print(b)
# c=[]
# for j in a.values():
#         c.append(j)
# print(c)
