my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for i in my_dict.values():
  for j in i:
    print(j,end=' ')
  print()

  # j=0
  # while j in i:
  #   print(j,end=' ')
  #   j=j+1
  # i=i+1












# Sample Output:
# C1 C2 C3                                                                                                      
# 1 5 9                                                                                                         
# 2 6 10                                                                                                        
# 3 7 11
