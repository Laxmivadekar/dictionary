a= {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}    # b=[]
    # for v in a.values():
    #     b.append(v)
    # d=[1]
    # e=[]#for using storing the keys
    # for i in a:
    #     c=[]
    #     j=0
    #     while j<len(b):
    #         if len(b[j])==len(d):
    #             e.append(i)
    #         j=j+1
    # print(e)
b=[]
c=[1]
for i in a:
    s=i
    for j in a:
        if len(c)<=len(a[i]):
            s=j
    b.append(s)
            
print(b)

#  Shortest list of values with the keys of the said dictionary: ['VI', 'VIII', 'X']
