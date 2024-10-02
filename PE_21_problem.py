


def sum_divisors(num):
    summ=1
    for i in range(2,num):
       if num%i == 0:
           summ+=i
           
    return summ       
           

def amicable_finder(num):
    amicas=[]
    for n in range(num):
        print(n)
        div_sum=sum_divisors(n)
        print(div_sum)
        is_am=sum_divisors(div_sum)
        print(is_am)
        if n==is_am:
            if n not in amicas:
                amicas.append(n)
            if div_sum not in amicas:                
                amicas.append(div_sum)
    return amicas


def summer_amicable(num):
    nums=amicable_finder(num)
    print(nums) 
    sum_amicas=sum(nums)   
    return sum_amicas

# print(summer_amicable(1000))
# print(sum_divisors(220))

# [1, 6, 28, 220, 284, 496]
# 1035