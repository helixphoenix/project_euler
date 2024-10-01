# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

triangle_1=[
[75],
 
[95, 64],

[17, 47, 82],

[18, 35, 87, 10],

[20,4, 82, 47, 65],

[19, 1, 23, 75, 3, 34],

[88, 2, 77, 73, 7, 63, 67],

[99, 65, 4, 28, 6, 16, 70, 92],

[41, 41, 26, 56, 83, 40, 80, 70, 33,],

[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],

[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],

[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],

[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],

[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],

[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

def max_straight_liner(lines:list):
    sums=[]
    for line in lines:
        sums.append(sum(line))
    return max(sums)

#adjacent: solution for only straight from second row

def triangler_row2(tri):
    line1=[tri[0][0]]
    line2=[tri[0][0]]
    tri.remove(tri[0])
    for row in tri:
       line1.append(row[-1])
       line2.append(row[-2])
    straight_lines=[line1,line2]   
    # print(straight_lines)
    return straight_lines
    
    
def maxfirsttwo(tri):
    
    sorted_lines= triangler_row2(tri)
    base=sorted_lines[1][0]+sorted_lines[1][1]
    max_sum=max_straight_liner(sorted_lines)
    
    return max_sum, base
    
    
# print(maxfirsttwo(triangle) )  #792


#adjacent: solution for straight from each row

def triangler(tri):
    triangle=tri
    triangle.remove(triangle[0])
    max_sum,base=maxfirsttwo(triangle)
    tmp_sum=0
    row=2
    while triangle:
        for r in range(len(triangle)):
            tmp_sum+=base+triangle[r][-row-1]
        if tmp_sum>max_sum:
            max_sum=tmp_sum   
        base+=triangle[0][0]
        triangle.remove(triangle[0])
        row+=1
    return max_sum

   
print(triangler(triangle_1)) #30525 this can be used to solve problem 67 too
 