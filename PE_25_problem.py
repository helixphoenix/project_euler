# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89
# 144
# The 12th term, is the first term to contain three digits.
# The Fibonacci sequence is defined by the recurrence relation:
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

def digital_fibonacci(digit_length):
    index=12
    term=144
    previous=89
    while len(str(term))<digit_length:
        new_term=previous+term
        previous=term
        term=new_term
        index+=1
        print(previous,term,index)
    if len(str(term))==digit_length:
        return print(index)
        
# digital_fibonacci(1000)  4782

