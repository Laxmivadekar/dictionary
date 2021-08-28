# a=[1, 2, 3, 4]
# d=b={}
# i=0
# while i<len(a):
#     d[i]={}
#     d=d[i]
#     i=i+1
# print(b)
    
r=1
s=9
A=65
while r<=5:
	print(' '*s,end='')
	c=r
	while c>1:
		print('',chr(A),end="")
		c-=1
		A+=1
	k=1
	while k<=r:
		print(' ',chr(A),end=" ")
		k+=1	
		A+=1
	print()	
	r+=1
	s-=2












# Sample output:
# {1: {2: {3: {4: {}}}}}