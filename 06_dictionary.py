#dictionary is used to store key : value pairs
#they are unordered ,mutable(changable) and dont allow duplicate keys

student = {
    "Name" : "Nikita",
    "Degree" : "B.Tech",
    "Age" : 22,
    "is_adult" : True,
    "Marks" : [90,80,95],
    "Language" : ("C++","Pyhton","HTML"),
    1 : "Namaste"
}

print(student)
print(type(student))
print(student["Name"])
print(student["Degree"])
print(student[1])
print(student["Language"])
# print(student["abc"])   this will give error

student["Name"] = "Nikki"
print(student)

#nested dictionary
Stu = {
    "name" : "Ansh Yadav",
    "info":{
       "age" : 23,
       "race" :"Indian",
       "Sub_opted" : ["Chem","Physics","Maths"] 
    }
}

print(Stu["info"])
print(Stu["info"]["age"])

#Dictionary Methods  myDic.keys() ,myDic.values() ,myDic.items() ,myDic.get("key") , myDic.update(newDic) 

print(student.keys())   #retuen in list format
print(student.values()) 
print(student.items())  # returs key value pairs as tuples  (key , value)
# we can typecast it too
print(list(student.items()))

pairs = list(student.items())   #without adding list it wont work
print(pairs[0])
print(len(student))

print(student.get("Name"))

print(student.get("abcd"))  # this will return none
# print(student["abcd"])   # this will give error

student.update({
    "city": "Delhi"
})

print(student)
