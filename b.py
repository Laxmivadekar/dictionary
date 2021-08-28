d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("key   value   count")
i=0
count=0
while count,(key,value) in enumarate(d.items(),i):
    i=i+1
    count=1
    print(key,'  ',value,'  ',count)



# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# print("key  value  count")
# for count, (key, value) in enumerate(dict_num.items(), 1):
#     print(key,'   ',value,'    ', count)
# Sample Output:
# key  value  count                                                                                             
# 1     10      1                                                                                               
# 2     20      2                                                                                               
# 3     30      3                                                                                               
# 4     40      4                                                                                               
# 5     50      5                                                                                               
# 6     60      6

