# Largest palindrome product
# Show HTML problem content 
# Problem 4
# A palindromic number reads the same both ways.
# The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made 
# from the product of two 3-digit numbers.


def is_palindrome(num):
    return (list(num)[:3]==list(num)[:2:-1])

def find_palindrome(num):
    for j in range(899): 
       if is_palindrome(str(num * (999-j))):
         return (num * (999-j))
    return None 

def largest_palindrome():
       for k in range(899): 
          t= find_palindrome(999-k)
          if t!=None:
              return print(t)
          

largest_palindrome()        
        
        
    
    
    
    