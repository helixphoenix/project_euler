
# Starting with the number 1
#  and moving to the right in a clockwise direction a 
#  by 
#  spiral is formed as follows:

# 72                     79   261+57+64+71+78  =261+270   531
# # 43   44 45 46 47 48 49 50   101+31+37+43+49 261 ==>7 by 7 . 101+150
# # #   [21 22 23 24 25]26 51
# # #   [20  7  8  9 10]27 52
# # #   [19  6  1  2 11]28
# # #   [18  5  4  3 12]29
# # #   [17 16 15 14 13]30
# # 37  36 35  34 33 32 31 56
# 65 64                     57 85

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

def create_dia_square(diago:int):
    dia=101
    n=4
    diag=25
    while n<diago-1:
        n+=2
        corner=0
        while corner<4: 
            print("n",n)
            diag=diag+n
            print("dia",diag)
            dia+=diag
            corner+=1
            # print(corner)
    return dia


# dia=create_dia_square(6)
# print(dia) 


# dia=create_dia_square(9)
# print(dia)


# dia=create_dia_square(11)
# print(dia)

# dia=create_dia_square(1001) 669171001
# print(dia)
# print(1001*1001)