# A unit fraction contains 1  in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

 
# Where 
#  means 
# , and has a 
# -digit recurring cycle. It can be seen that 
#  has a 
# -digit recurring cycle.

# Find the value of 
#  for which 
#  contains the longest recurring cycle in its decimal fraction part.

def find_pattern(num):
    numstr=str(num)[2:]
    pattern=str()
    for i in range(len(numstr)):
        if numstr[i]in numstr[i+1:] and numstr[i] not in pattern:
            pattern+=numstr[i]
            # print(pattern)
    return len(pattern)
 
def longest_recurring(highest_divisor):
    longest=len(str(142857))
    value=7
    for num in range(7,highest_divisor):
        val=1/num
        length_pattern=find_pattern(val)
        # print(length_pattern)
        if longest<length_pattern:
             longest=length_pattern
             value=num
             print("here",longest,value)
    return {value:longest}         

# print(find_pattern(0.14285714285714285))
# print(longest_recurring(1000)) d=405 9 digit reccurring part