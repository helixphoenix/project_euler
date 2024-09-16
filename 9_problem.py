# A Pythagorean triplet is a set of three natural numbers, a<b<c
# , for which, a^2+b^2=c^2

# For example, 9+16=25
# .

# There exists exactly one Pythagorean triplet for which a+b+c=1000
# .
# Find the product a*b*c
# .
# a+b+c=1000

# a [3,325]
# b[4,351]
# c [0,993]

def is_triplet(a,b,c):
    if (a*a)+(b*b)==(c*c):
        # print(a,b,c,(a+b+c))
        return 1000
    else:
        return 0

def pythagorean_trip():
        for a in range(0,1000):
            for b in range(0,1000):
                for c in reversed(range(0,1000)): 
                    if a<b<c and (a+b+c)==is_triplet(a,b,c):
                        return [a,b,c,(a*b*c)]
                    
                    
pytha_triplet_set=pythagorean_trip()
print("magic triplet:",pytha_triplet_set) #[200, 375, 425, 31875000]
    