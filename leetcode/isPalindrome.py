## Palindrome Problem : 


#By converting to string
def is_palindrome_00(x: int) -> bool:
    y = str(x)
    n = len(y)
    for i in range(int(n/2)):
        if y[i] != y[n-1-i] :
            return False
        
    return True

#Without converting to string and reverse the whole number
def is_palindrome_01(x: int) -> bool :
    if x<0 : 
        return False 
    
    y = 0
    
    tmp = x

    while tmp > 0 :
        d = tmp % 10
        tmp = (tmp - d) / 10
        y = y*10 + d
        print(y)
    

    return int(y) == x


# Reverse only half of it
def is_palindrome_02(x: int) -> bool:
    
    if x < 0 or (x%10 == 0 and x!=0) : 
        return False
    
    if x < 10:
        return True

    y = 0
    while y < x :
        d = x % 10
        x =  (x-d) / 10
        y = y*10 + d
    
    #Odd number of digits
    return x == y or int(y/10) == x



print(is_palindrome_02(121))