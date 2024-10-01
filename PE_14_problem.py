# The following iterative sequence is defined for the set of positive integers:

#  (n->n/2 (n is even)
#  (n -> 3n +1 (n is odd)

# Using the rule above and starting with, we generate the following sequence:

# It can be seen that this sequence (starting at and finishing at ) contains terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at .

# Which starting number, under one million, produces the longest chain ?

# NOTE: Once the chain starts the terms are allowed to go above one million.



# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 



def chainer(num):
    chain=[num]
    
    while num>1:
                 
        if num%2==0:
            num=num/2
            print(num)
            chain.append(num)

        elif num%2!=0:
            num = 3*num+1  
            print(num)      
            chain.append(num)  
    if  num==1:
        chain.append(num)   
    print(chain)    
    return len(chain)



def longest_collatz(num):
    clen=0
    for n in reversed(range(num)):
        print(n)
        tmp=chainer(n)
        if tmp > clen:
            clen=tmp
            
    print(clen)        
    return clen        
            
        
length=longest_collatz(1000000)

print("max",length)

# max 526