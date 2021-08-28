student={'name':'Lucky','age':21,'courses':['math','stats','comsci']}
print(student)

#=============
print(student['name'])
# print(student['phone']) in the above studentdictionary phone key 
# and( for that key value is not there thats why nits gives error
print(student['age'])
print(student['courses'])

print(student.get('phone')) #it gives none because we didn't pass value for that
print(student.get('phone','not found')) #it gives 'not found' because we pass alternate value like sentence


student['phone']='555.5555'
print(student['phone'])

# we want to update multiple values means we will use update keyword
student.update({'name':'Laxmi','age':22,'courses':['maths','science','history']})
print(student)

#we want to delete any particular key or value of that key
courses=student.pop('courses')
print(student)
print(courses)

#we want to see how many keys and values are there in our dictonary
#we will use print(dict.keys()) and print(dict.values())

print(student.keys())
print(student.values())
print(student.items())
print(type(student))


student=dict(name= "Ravina",age= 20)
print(student) 

#dictionary inside another dictionary
Dic= {
 1: 'NAVGURUKUL',
 2: 'INSIDE',  
 3:{
     'A' : 'WELCOME',
     'B' : 'To', 
     'C' : 'BANGALUR CAMPUS'
     }
}
print(Dic) 


#by using loops
for key in student:
    print(key)
#=====
# i=0
# while key in student:
    # print(key)
person={
    'name':'jack',
    'age':20,
    'gender':'male',
    4:'organisation'}

result = person['age'] 
x = person.get("gender")
print(person[4])
print(x)
print(result) 

#======================================
states_capitals = {
  'Gujarat' : 'Gandhinagar',
  'Maharashtra' : 'Mumbai',
  'Rajasthan' : 'Jaipur',
  'Bihar' : 'Patna'
  }
for capital in states_capitals:   #(or )for state in states_capitals:
    print(capital)     #(or) print(state) it is also gives same output
