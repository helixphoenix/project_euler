# The sum of the squares of the first ten natural numbers is,

# 1
# 4
# 9
# 16  --30
# 25
# 36
# 49 --110
# 64
# 81 --145
# 100
# ----- 385

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 55^2 --- 3025


# The square of the sum of the first ten natural numbers is,

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def squaring_the_naturals(num):
    sum=0
    for i in range(1,num+1):
        sum=sum+(i*i)
    return sum



def squaring_the_sum(num):
    sum=0
    for i in range(1,num+1):
        sum=sum+(i)
    return sum*sum    




def differing_the_squares(num):
    a=squaring_the_naturals(num)
    b=squaring_the_sum(num)
    return b-a



print(differing_the_squares(100))