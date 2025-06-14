str1 = "this is a string.\nAnd this will be printed in next line"
print(str1)
str2 = "Tab space\ttab space"
print(str2)

# Basic string operations
name = "Nikita "
surname = "Rathore"
print(name+surname)

#length of string
print(len(name),"and", len(surname))

            # str1[3] = "b"  this thing is not allowed in python

#Slicing
name = "Nikita rathore"
print(name[1:6])  # this will print string from index 1 to 6  i.e ikita
print(name[1:len(name)])
print(name[:5])  #it mean[0:5]
print(name[5:])  #it means [5:len(name)]

#negative index exist only in python for eg hello ="hola" a-> -1 , l-> -2, o->-3 , h->h
print(name[-1])

print(name[-3:-1])  # it will only print -3 and -2 not -1


# types of string function eg -> str.endswith("ta") , str.capitalize() , str.replace(old,new) ,str.find(word) , str.count("abc")

sentence = "i am Nikita Rathore"
print(sentence.capitalize())  # this will temporary capitalize the string firdt letter

sentence = sentence.capitalize()  # this will permanently capitalize
print(sentence) 

print(sentence.endswith("Nikita"))
print(sentence.endswith("athore"))  # this is printing false for "Rathore" and true for "athore"
print(sentence.replace("i","o"))
print(sentence.replace("nikita","Nikki"))

print(sentence.find("nikita"))  #this will return the index at which nikita is starting
print(sentence.find("Nikita"))

print(sentence.count("a"))   #prints int value





#homework question
# name = input("Enter the name : ")
# print("name is ", name)
# length = len(name)
# print("and the length of name is ",length)
