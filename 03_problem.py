# Largest prime factor
# Show HTML problem content 
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

from problem7 import extracted_primez

def prime_fact(num):
    # primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i in reversed(extracted_primez):
        if num % i == 0:
            return print(i)
                
prime_fact(600851475143) #6857       