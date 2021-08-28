# list=[]
# i=1
# while i<=5:
#     w=int(input('enter a number'))
#     list.append(w)
#     i=i+1
list=[22,33,44,55,66]
d={}
i=0
while i<len(list):
    s=str(list[i])
    j=0
    string=''
    while j<len(s):
        if s[j]=="0":
            string+='zero'
        elif s[j]=="1":
            string+='one'
        elif s[j]=="2":
            string+='two'
        elif s[j]=="3":
            string+='three'
        elif s[j]=="4":
            string+='four'
        elif s[j]=="5":
            string+='five'
        elif s[j]=="6":
            string+='six'
        elif s[j]=="7":
            string+='seven'
        elif s[j]=="8":
            string+='eight'
        elif s[j]=="9":
            string+='nine'
        j=j+1
    # i=i+1
    d[list[i]]=string
    i=i+1
print(d)
            
