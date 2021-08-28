# x = ({'Math':81, 'Physics':83, 'Chemistry':87})
# d={}
# for i,j in x.items():
#     if x[j]>x[j+1]:
#         d[i]=x[j]
# print(d)

print('_____________________________________')
# a= ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
# b=[1, 2, 2, 3]
# d={}
# c={}
# for i in a:
#     c[a[i]]=b[i]
# d.update(c)
# print(d)
    

# Output: defaultdict(<class 'set'>, {'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}})


from collections import defaultdict
a = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
b = [1, 2, 2, 3]
temp = defaultdict (set)
for i, j in zip(a,b) :
    temp[ i ].add ( j )

print (temp)

