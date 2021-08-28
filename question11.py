my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
a=[]
for i in my_dict.values():
    if my_dict[i]>50:
        a.append(my_dict[i])
print(a)


# Output :-
# [58,56,100]
