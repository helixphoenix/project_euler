# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 28, which means that is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 16, the smallest number that can be written as the sum of two abundant numbers is 24
# . By mathematical analysis, it can be shown that all integers greater than 
#  can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that 
# cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from PE_21_problem import sum_divisors

def is_abundant(num):
    abundant_list=[]
    for n in range(num+1):
        dsumm=sum_divisors(n)
        if dsumm>num:
           abundant_list.append(n)
    return abundant_list

def sum_ab(num):
    ab_sum=[]
    abu=is_abundant(num)
    for a in abu:
        for b in abu:
            # print(a,b,(a+b))
            if (a+b) not in ab_sum:
                ab_sum.append((a+b))
    return ab_sum

def non_abundant_summer(num):
    summ=0
    sum_abu=sum_ab(num)
    for n in range(num+1):
        if n not in sum_abu:
            summ+=n
    return summ      
        
    
# print(is_abundant(28123))
# print(sum_ab(28123))
# print("sum_of_non_abundant",non_abundant_summer(28123)) sum_of_non_abundant  386442386