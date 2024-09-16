# Even Fibonacci numbers
# Show HTML problem content 
# Problem 2
# Each new term in the Fibonacci sequence is generated
# by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence
# whose values do not exceed four million, 
# find the sum of the even-valued terms.
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

def even_fibonacci(limit):
    sum=0
    prev=1
    f=2
    p=0
    while f < limit:
        # print(f)
        if f%2==0:
            # print(f)
            sum=sum+f
            print(sum)
        p=f    
        f=prev+f 
        prev=p
    return print("sum:",sum)       

even_fibonacci(4000000)
 
             
# 2
# 10
# 44
# 188
# 798
# 3382
# 14328
# 60696
# 257114
# 1089154
# 4613732
# sum: 4613732        
                