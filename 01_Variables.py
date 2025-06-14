print("Nikita you are sweetest")
name = "Nikita"
age = 22
price_of_outfit = 755.5

print("Name is ",name," and age is ",age," and she is wearing a kurti today of worth ", price_of_outfit)

college = None
graduated = False

print(type(name))
print(type(age))
print(type(price_of_outfit))
print(type(college))
print(type(graduated))

# hello this is a comment

# Operators
a = 2
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a/b)  # division always gives float value
print(b/a)  # returns 2.0
print(a%b)
print(b%a)
print(a**b)  # a^b
print(b**a)

# relational operators
print(a==b)  # o/p -> False
print(a!=b)
print(a>b)
print(a>=b)
a = a+ 10  # a+=10
print(a)

num = 10
num = num**5  # num**=5 
print(num)

# logical operators
c = 5
d = 6
print(not False)
print(not True)
print(not (c>d))
print(not (d>c))
val1 = True
val2  =  False
print( val1 and val2)
print(val1 or val2)

# taking input from user
# input("Enter your name : ")

name = input("Enter name again : ")
print("Welcome ",name)

value = input("enter some value ")
print(type(value))  # input type always returns string
# that is why we have to specify the type of input 

value = int(input("Enter the value of int "))
print(type(value))