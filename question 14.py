# {'bijender':45,'deepak':60,'param':20,';'anjili':30,'roshini':50}

# Expected result in Ascending Order:

# {'param':20,'anjili':30,'bijender':45,'roshini':50,'deepak':60}

# Expected result in Descending Order:

# {'deepak':60,'roshini':50,'bijender':45,'anjili':30,'param':20}
d={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
for i in d:
    for j in d:
        if d[i]<d[j]:
            d[i],d[j]=d[j],d[i]
print(d)
print('_____________________________________')
d={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
for i in d:
    for j in d:
        if d[i]>d[j]:
            d[i],d[j]=d[j],d[i]
print(d)


