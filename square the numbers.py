n=int(input("Input a number "))
d = dict()
i=1
while i<=n:
    d[i]=i*i
    i=i+1
print(d) 
#0r
c=dict()
for i in range(1,16):
    c[i]=i*i
print(c)  #or

d=dict()
n=2
i=1
while i<=5:
    d[i]=n*i
    i=i+1
print(d)


a = []
if not a:
  print("List is empty")


my_dict = {}
if not (my_dict):
    print("Dictionary is empty")
	

from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)
#or
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d={}
for i in d1:
    for i in d2.items():
        if d1[i].keys()==d2[i].keys():
            d[i]=d1[i]+d2[i]
        elif d1[i]!=d2[i]:
            d[i]=d1[i]
        else:
            d[i]=d2[i]
print(d)













# for x in range(1,n+1):
#     d[x]=x*x
# print(d) 
# Sample Output:

# 10                                                                                                            
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}   
