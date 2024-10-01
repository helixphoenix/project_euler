# Smallest multiple
# Show HTML problem content 
# Problem 5
# 2520 is the smallest number that can 
# be divided by each of the numbers 
# from 1 to 10 without any remainder.

# What is the smallest positive number 
# that is evenly divisible by all of the numbers from 1 to 20?      
# division_group=[7,11,13,16,17,9,19,5] for 20
# division_group=[5,7,8,9] for 10


#checks if needed        

def is_prime(number:int):
    prime_numbers=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                   211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397]
    if number in prime_numbers:
        return True
    else:
        return False        

def is_square_and_quadrant(number:int):
    square_numbers=[4,8, 9, 16, 25,27, 36, 49, 64, 81, 100, 121,125, 144]   
    if number in square_numbers:
        return True
    else:
        return False     
    

            
def square_quadrant_check(multiplied:int,square_numbers:list,ind:int):
      if multiplied%square_numbers[ind]==0:
            res=multiplied/square_numbers[ind]
            return res
      else:
          return 0

def divide_check(num,multiplied):
    for i in range(1,num):
        print(multiplied/i)

  
def double_check(multi_num, squares, primes): 
    for i in range(len(squares)):
        res= square_quadrant_check(multi_num,squares,i)
        print(res,i)
        if res%primes[i]==0:
            res=multi_num/primes[i]
            # divide_check(10,res)
            if squares[i]==4:
                res= square_quadrant_check(multi_num,squares,i)
                if res%2==0:
                    multi_num=multi_num/2             
                    print("2",multi_num)    
    return multi_num           

#multiplication of divisibles=biggest(squares+quadrantes all the power ofs)+primes

def multiply_divisible(divisibles:list):
    multip=1
    for num in divisibles:
        multip=multip*num
    return multip    
     


def smallest_multiple(squares,primes):
    divisibles= squares+primes
    res=multiply_divisible(divisibles)
    # print(res)
    # divide_check(10,res)
    reduced_res=double_check(res,squares,primes)
    # print("-------------------------")
    # divide_check(10,reduced_res)
    if res==reduced_res:
        return res
    else:
        return reduced_res   
    

print("Result:",smallest_multiple([9,16],[5,7,11,13,17,19]))
# Validation with example 2520
print("Result:",smallest_multiple([8,9],[5,7]))
