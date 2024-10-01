# What is the sum of the digits of the number 2^1000? n^k


def empowerment(n,k):
    power=k
    num=n
    while power>1:
        num*=n
        power-=1
        print(power,num)
    return str(num)    


def sumarizer(num:str):
    sum=0
    for n in num:
        sum+=int(n)
    return sum    

numb=empowerment(2,1000)        
# numb=empowerment(2,500)     
print(sumarizer(numb))      
# 1366

