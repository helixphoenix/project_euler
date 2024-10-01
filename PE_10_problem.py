# The sum of the primes below 10 is 2+3+5+7=17.

# Find the sum of all the primes below two million.

from PE_07_problem import extracted_primez,prime_check

def prime_summer(known_primes,unknown_start,unknown_end):
    unknown_primes=prime_check(unknown_start,unknown_end)
    all_the_primes=known_primes+unknown_primes
    print(all_the_primes)
    return sum(all_the_primes)



sum=prime_summer(extracted_primez,999984,2000000)
print("sum",sum)   #sum 218014632968