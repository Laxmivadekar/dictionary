a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
for i in a.values():
    for j in a.values():
        if j<j+1:
            temp=j
            j=j+1
            j+1=temp
    #     j=j+1
    # i=i+1
print(a)





# Expected result in Ascending Order:
# {'param':20,'anjili':30,'bijender':45,'roshini':50,'deepak':60}
# Expected result in Descending Order:
# {'deepak':60,'roshini':50,'bijender':45,'anjili':30,'param':20}
