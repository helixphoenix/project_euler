# Largest palindrome product 
# Problem 4
# A palindromic number reads the same both ways.
# The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made 
# from the product of two 3-digit numbers.


def is_palindrome(num):
    rev_num=list(num)
    rev_num.reverse()
    return (list(num))==rev_num


def  search_palindrome():
    big_one=0
    f=open("big_palindromes.txt","a")
    for p in reversed(range(100,1000)):
        for k in reversed(range(100,999)):
            prod=p*k
            if is_palindrome(str(prod)) and prod>big_one:
               f.write(str([prod,p,k,is_palindrome(str(prod))]))
               big_one=prod
    return big_one
                 




big=search_palindrome()        
print(big)   #[906609, 993, 913, True]
# print(is_palindrome(str(9009)))
    
    
    