# What is the value of the first triangle number to have over five hundred divisors?


    
    
    
def find_divisor(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1      
    return count        

        


def fivehundered_checker():
    triangle= 55
    term= 10
    count= 4

    while count <= 1000:
        term=term+1
        triangle=triangle+term
        count = find_divisor(triangle)
        print("count",count)
        print("triangle",triangle)
        print("term",term)
        if count> 500:
            return triangle    


triangle_500= fivehundered_checker()        
print(triangle_500)        

# count 576
# triangle 76576500
# term 12375  
       
