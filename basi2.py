#how dictionary prints keys and values together
movie ={
    "name":  "Puli",
    "hero":  "Vijay",
    "rating":  7.5
    }
for x,y in movie.items():
    print(x,y) 
print()
#=========================if we will take the condition like this
for x in movie:
    print(x)
