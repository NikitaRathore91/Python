def show(n):
    if(n==0) :
        return
    print(n)
    show(n-1)
    
# factorial

def factorial(n) :
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1);     
     