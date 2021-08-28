#Q48.Write a Python program to find the length of a given dictionary values. 
# Original Dictionary
a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# b=list(a.values())
d={}
for i,j in a.items():
    c=len(j)
    d[j]=c
print(d)

d={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
d={}
for i,j in d.items():
    d[i]=j
print(d)
    




# Convert the said dictionary into a list of lists:
# [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
# Original Dictionary:
# {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# Convert the said dictionary into a list of lists:
# [['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]














# Length of dictionary values:
# {'red': 3, 'green': 5, 'black': 5, 'white': 5}

