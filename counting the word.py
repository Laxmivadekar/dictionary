count = {"M":0,"I":0,"S":0,"P":0}
word = "MISSISSIPPI"
for i in word:
	if i == "M":
		count['M'] = count['M']+1
	elif i == "I":
		count['I'] = count['I']+1
	elif i == "S":
		count['S'] = count['S']+1
	elif i == "P":
		count['P'] = count['P']+1
print( count)

#=================================
word = "MISSISSIPPI"
d={}
i=0
while i<len(word):
	j=0
	count=0
	while j<len(word):
		if word[i]==word[j]:
			count+=1
		j=j+1
	d[word[i]]=count
	i=i+1
print(d)

# {M:1,I:4,S:4,P:2} :o/p
#===============================
a='w3resource'
d={}
i=0
while i<len(a):
	j=0
	count=0
	while j<len(a):
		if a[i]==a[j]:
			count+=1
		j=j+1
	d[a[i]]=count
	i=i+1
print(d)



# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}