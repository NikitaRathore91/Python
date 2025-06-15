#defining a function
def calc_sum(a,b):    #a,b ->parameters
    sum = a+b
    print(sum)
    return sum

def printHello(n):
    for i in range(0,n) :
        print("Hello")

        
calc_sum(5,10)  #argument1,argument2
calc_sum(10,15)

printHello(5)   #this prints hello 5 times

# built in functions-> print(),len(),type(),range()
#user defined function -> we write

# default arguments :- by deafault this values will be used if no values are passed while function calling

def cal_prod(a = 2,b =4):   # def(a,b = 4) this will also work
    print(a*b)              # def(a = 4,b) this will give error
    return a*b

cal_prod(5,5)   #this will print 25
cal_prod()   #this will print 8
cal_prod(5)   #this will print 20
