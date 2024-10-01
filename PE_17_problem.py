
three_digits=10
four_digits=8

def baser(n)->int:
    num=int(n)
    if num in[3,7,8]: 
        return 5
    elif num in [1,2,6,10]:
        return 3
    elif num in [4,5,9]:
        return 4
    elif num in [11,12]:
        return 6
    elif num in [13,14,17,18,19]: 
        return 8
    elif num in [15,16]:
        return 7
    elif num ==17:
        return 9
    
def twor(n)->int:
    num=int(n)
    if num==7: 
        return 7
    elif num in [2,3,8,9]:
        return 6
    elif num in [4,5,6]:
        return 5
    
    
      



def two_digiter(word)-> int:
    count=0
    num=int(word)
    if num<20:
        count+=baser(num)
    elif 20<=num<100:
        if int(word[1])==0:
            count+=twor(word[0])
        else:  
         count+=twor(word[0])+ baser(word[1])
    return count 


def three_digiter(word)-> int:
      count=0
      count+=baser(word[0])+three_digits

      if word[1:3]=="00":
          return count   
      elif int(word[1])==0:
          count+=baser(word[2]) 
      else:    
       count+=two_digiter(word[1:3])
      return count
      

def letter_counter(ranger:tuple):

    lcount=0
    for num in reversed(range(ranger[0],ranger[1]+1)):
        word=str(num)
        if num==1000:
            lcount+=int(baser(int(word[0])))+ four_digits

        elif 100<=num<1000:

            lcount+=three_digiter(word)
        else:
            lcount+=two_digiter(word)
    return lcount


# print("letter_count",letter_counter((1,1000)))   21141



# print("letter_count",letter_counter((1,5)))
                            
      

# print(baser("18"))

# print(three_digiter("324"))

# print(two_digiter("35"))

# print(twor(3))

# print(letter_counter((1,5)))

# print(letter_counter((1,25)))

# print(letter_counter((1,324)))

