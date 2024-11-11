from PE_15_problem import factorial


# print(factorial(len(digits))) 3628800
# 3628800/10=362880 X2 =>1
# 362880/9=40320 X X6 =>6
# 40320/8=5040 X6 =>7
# 5040 / 7 = 720 X2 =>2
# 720 / 6 = 120 X5 =>8
# 120/5=24 X1 =>0
# 24/4=6 X2 =>4
# 6/3=2   X2 =>3
# 2/2=1   X2 =>9
# 1/1=1   X1 =>5
# millionth

#1672804395  milionth

# [1] [0, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 6] [0, 2, 3, 4, 5, 7, 8, 9]
# [1, 6, 7] [0, 2, 3, 4, 5, 8, 9]
# [1, 6, 7, 2] [0, 3, 4, 5, 8, 9]
# [1, 6, 7, 2, 8] [0, 3, 4, 5, 9]
# [1, 6, 7, 2, 8, 0] [3, 4, 5, 9]
# [1, 6, 7, 2, 8, 0, 4] [3, 5, 9]
# [1, 6, 7, 2, 8, 0, 4, 3] [5, 9]
# [1, 6, 7, 2, 8, 0, 4, 3, 9] [5]
# [1, 6, 7, 2, 8, 0, 4, 3, 9, 5] []
# 1672804395


digits=[0,1,2,3,4,5,6,7,8,9,]
  
def add_value(current_value,fact_length):
    d=0
    if 1000000-current_value<=2 and fact_length==1:
        if 1000000-current_value==2:
            d=2
            current_value+=1
        else:    
            d=1  
            current_value+=1 
        return [d,current_value]
    while current_value<1000000:    
        current_value+=factorial(fact_length)
        d+=1   
    if current_value>=1000000:
        current_value-=factorial(fact_length)
        d-=1 
  
    # print("add",current_value, d,factorial(fact_length))         
    return [d,current_value]

def exhaust_numbers(digit_list,current_value,num_of_digits):
    nums=[]
    digitis=digit_list
    while nums!=len(digit_list) and num_of_digits>=0:  
        #  print("exhaust",current_value,num_of_digits)
         val = add_value(current_value,num_of_digits)
         if val[0]>=1 and len(digitis)>1 :
            nums.append(digitis[val[0]-1])
            digitis.remove(digitis[val[0]-1])
         elif len(digitis)==1:
            nums.append(digitis[0])
            digitis.remove(digitis[0])     
         num_of_digits-=1
         current_value=val[1]
         print(nums,digitis)
    return nums

def create_num(nums):
    num=str()
    for n in nums:
       num= num+str(n)
    return int(num)

def one_in_a_milion(digits):
    num_of_digits=len(digits)-1
    current_value=0
    nums=exhaust_numbers(digits,current_value,num_of_digits)
    num=create_num(nums)       
    return num

print(one_in_a_milion(digits))