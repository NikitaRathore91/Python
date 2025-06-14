# if elif else

color = input("enter the color : ")

if(color=="Pink"):
    print("Color is pink")
elif(color=="Green"):
    print("Color is Green")
elif(color=="Blue"):
    print("Color is blue") 
else:
    print("no color matches")         
    
print("Code ends")      

marks = 76
grade = None

if(marks>90):
    grade = "A"
elif(marks<90 and marks>=80):
    grage = "B"
elif(marks<80 and marks >=70):
    grade = "C"
elif(marks<70 and marks>=0):
    grade = "D"

print("Grade is ",grade)                