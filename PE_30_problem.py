# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
 
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4

# 1634+8208+9474 = 1^4 + 6^4 + 3^4 + 4^4 + 8^4 + 2^4 + 0^4 + 8^4 + 9^4 + 4^4 + 7^4 + 4^4
# 19316 = 0^4 + 1^4 + 2^4 + 3^4 + 3.4^4 + 6^4 + 7^4 + 2.8^4 + 9^4

# 3*9^4
# 4*9^4
# 5*9^4
# 6*9^4


# As is not a sum it is not included.

# The sum of these numbers is .

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def power_on(l,p):
    pow=1
    k=0
    n=int(l)
    while k<p:
        pow*=n
        k+=1
        print(k)
    return pow

def p_power_sum(number:list,p):
    sum=0
    for n in number:
        sum += power_on(n,p)
    return sum    

# print(power_on(9,3))
# print(power_on(9,4))
# print(power_on(9,5))
# print(power_on(9,6))

# print(5*59049) 295245
def ranger (p):
    rang1="1"
    rang2="9"
    while len(rang1)<p:
        rang1+="3"
        rang2+="8"
    return int(rang1),int(rang2)
        
def search_p_power_sum_numbers(p):
    rang1,rang2=ranger(p)
    print(rang1)
    power_numbs=[]
    for n in range(rang1,rang2):
        print(n)
        if n==p_power_sum(list(str(n)),p):

           power_numbs.append(n)
           print(power_numbs)
    print(power_numbs)
    
    return(sum(power_numbs))

# print(search_p_power_sum_numbers(4))
# [1634, 8208, 9474]
# 19316

# print(search_p_power_sum_numbers(5))
# [54748, 92727, 93084]
# 240559

# print(ranger(5))(13333, 98888)