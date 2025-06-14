#While loop

num = (1,2,3,4,5,6,7,8,9)
length = len(num)
x = 5

i = 0
while i<length :
    if(num[i]==x):
        print("Found")
        break
    i = i+1        

#break
#continue

j = 0
while j<=5 :
    if(j<=3):
        j = j+1
        continue    # when j <=3 further steps in loop will be skipped and it will start the loop again
    print(j)
    j=j+1   
    

# printing even numbers

i = 1

while i <= 10:
    if i % 2 != 0:
        i += 1
        continue  # Skip printing for odd numbers

    print(i, " ")
    i += 1  # Increment i after printing


#     FOR LOOPS
nums = (4,6,8,10,12)

for val in nums:
    print(val)    
    
    
# RANGE :-range function returns a sequence of numbers starting from 0 ny default, incremented by 1 and stops before specified number

r = range(5) # this means starts from 0 ends before 5 and step size 1
print("range 1")
for el in r:        #could have also written for el in range(10)
    print(el)

print("range 2")  
for el in range(2,6) :   #this means starts from 2 and ends befpore 6 and step size =1
    print(el)    

print("range 3")     # this means starts from 2 and ends before 10 and step size = 2
for el in range(2,10,2) :
    print(el)    
    
            