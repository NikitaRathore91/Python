marks = [98,57,78,40,33,80]
print("type of marks is ",type(marks))
print("Length of marks is ",len(marks))
print(marks)
print(marks[0])
print(marks[1])

student = ["Karan",97,"Mumbai"]

# Strings in python are immutable but lists are mutable

str = "hello"
# str[0] = "H"  this will give error but

student[0] = "Arjun" # this willl not give error

print(student)

#slicing in list
print(student[0:2]) # this will print arjun,97

# some functions for list
#list.append(4) , list.sort() , list.sort(reverse = true) ,list.reverse() , list.insert(index,element) , list.remove(1) ,list.pop(index)

numbers = [ 3,4,7,1,2,9]

numbers.append(0)
print(numbers)

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers.reverse()
print(numbers)

numbers.insert(5,5)
print(numbers)

numbers.append(3)
numbers.remove(3)  # it removes first occurence of 3 
print(numbers)


numbers.pop(3)  #this removes number at index 3