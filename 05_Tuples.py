# tuple is like list
# string and tuple are immutable  ie we can not change add elements in string and tuple
#list is mutable

tup =(2,3,5,6,2)
print(tup)
print("type of tup is -> " , type(tup))
print(tup[0])
print(tup[1],tup[2])

#we can crete empty tuple

tup1 = ()
print(tup1)
print("type of tup1 is -> " , type(tup1))

#to create a tuple of only one element we have to add a comma

tup2 = (1,)   # if we remove comma python will assume tup2 to be an int value 
print(tup2)

#slicing
print(tup[1:3])

# tup.index(num) ,tup.count(num)
print(tup.index(5))

print(tup.count(2))
