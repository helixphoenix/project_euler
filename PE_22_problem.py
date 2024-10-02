# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, 
# multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 53 , is the 938th name in the list. So, COLIN would obtain a score of 49714

# What is the total of all the name scores in the file?


alphabet={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

names=open("0022_names.txt","r").read()
names_list=names.replace('"',"").split(",")
# print(sorted(names_list))
s_name_list=sorted(names_list)
# print(s_name_list)
def letter_score(name):
    lscore=0
    for letter in name:
        lscore+=alphabet[letter]
    return lscore    

def name_score(names:list):
    nscore=0
    for row in range(len(names)):
        nscore+=(row+1)*letter_score(names[row])
    return nscore


# print(name_score((s_name_list)))    871198282
    

