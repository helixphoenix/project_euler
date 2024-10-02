from PE_15_problem import factorial

def string_list_summer(num:list):
    summ=0
    for n in num:
       print(n)
       summ+=int(n)
    return summ 
    
    

def fact_summer(num):
    fact=factorial(100)
    print(fact)
    number=list(str(fact))
    factsum=string_list_summer(number)
    return factsum
    
    
# print(fact_summer(100)) 648