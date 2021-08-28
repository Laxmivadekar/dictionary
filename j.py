# a={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
a= [1, 2, 3, 4]
b=c={}
for i in a:
    c[i]={}
    c=c[i]
print(b)


# Sample output:
# {1: {2: {3: {4: {}}}}}

# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
# Original Dictionary:
# {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# Filter even numbers from said dictionary values:
# {'V': [], 'VI': [], 'VII': [2]}
# 38.{'c1': 'Red', 'c2': 'Green', 'c3': None}
a={'c1': 'Red', 'c2': 'Green', 'c3': None}
for i in a.items():
    if 






# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}
