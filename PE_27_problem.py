
# b 997
# a 991
from PE_07_problem import extracted_primez


# |a|<1000 and |b|<=1000
# n^2+n+41+n^2-79n+1601 = 2n^2 -78n +1642   0<=2n<=79+39 ==>  n^2 -39n + 821 0<=n<=59
# a>n, n(a+n) +b
# a=n, b odd and  2n^2+b
# a=0, b odd and not prime  n^2+b
# a=-n,b must be prime      b
# a<n, n(a+n) +b
# a=1
# n^2+n+b == n^2+n+n+2 . == n^2+2n+2  b>=n+2
# a>=n .   0<n<=a  a>=n
# quad=(n*n)+(a*n)+b

# b>n, n(n+a) + b
# b!=n, n^2+(a+1)n . . n(n+a+1)
# b!=0, n(n+a)
# b!=-n,n(n+a+1)
# b<n, n(n+a) + b

# a+b=42
# a+b=1522

# a-b=40
# a-b=-1680

# b>n
# b>a 
# 0<n<|b|??? 1000
# a<n<|a| -1000
def quadratic_prime(a,b):
    ind=0
    for n in range(0,b):
      quad=(n*n)+(a*n)+b
      if quad in extracted_primez:
        # print("here",a,b,n)
        ind=n
      else:
        print("find another ab")
        return ind 
    return ind

# print(quadratic_prime(1,41))
# print(quadratic_prime(-79,1601))
    

def consequence():
    consec=[0,0]
    for b in range(-1000,1001):
         for a in reversed(range(-999,1000)):
           print(a,b)
           if a==1 and b==41:
               print("shout")
           n=quadratic_prime(a,b)
           print("quad",n)
           if n>consec[1]:
               consec=[(a*b),n]
    return consec 


print(consequence)
    
# print(quadratic_prime(1,41))
# print(quadratic_prime(-79,1601))

# n>39
# [a*b,n]
# # [-59231, 70]

# [a,b,n+1]
# [[1, 41, 40], [-1, 41, 41], [-3, 43, 42], [-5, 47, 43], [-7, 53, 44], [-9, 61, 45], [-11, 71, 46], [-13, 83, 47], [-15, 97, 48], [-17, 113, 49], [-19, 131, 50], [-21, 151, 51],
#  [-23, 173, 52], [-25, 197, 53], [-27, 223, 54], [-29, 251, 55], [-31, 281, 56], [-33, 313, 57], [-35, 347, 58], [-37, 383, 59], [-39, 421, 60], 
#  [-41, 461, 61], [-43, 503, 62], [-45, 547, 63], [-47, 593, 64], [-49, 641, 65], [-51, 691, 66], [-53, 743, 67], [-55, 797, 68], [-57, 853, 69], [-59, 911, 70], [-61, 971, 71]]