# Starting in the top left corner of a 2X2 grid, and only being able to move to the right and down, there are exactly routes to the bottom right corner.

# How many such routes are there through a 20x20 grid?



# Down first

# [0][0]  [0][1] [0][2] [1][2] [2][2]
 
# [0][0] [0][1] [1][1] [1][2] [2][2]
 
# [0][0] [0][1] [1][1] [2][1] [2][2]

# Right first
 
# [0][0] [1][0] [1][1] [1][2] [2][2]
  
# [0][0] [1][0] [1][1] [2][1] [2][2]
  
# [0][0] [1][0] [2][0] [2][1] [2][2]


def factoriel(n):
    fact=1
    for i in range(1,n):
        fact=fact*i
    return fact    
        
print (factoriel(20))

# 121645100408832000