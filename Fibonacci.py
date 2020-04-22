# A function to print fibonacci sequence of a given number

def fib(n):
    a = 0
    b = 1
    
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
            
 # Call the function to print first five numbers in the sequence
           
fib(5)          
