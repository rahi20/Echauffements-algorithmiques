# EOPI - Prob 1 : Convert Base
# We can assume that 2<= b1, b2 <=16


def convert_from_b10(s: str, b2: int) -> str :

    s_b2 = []
    num_b10 = int(s)
    while num_b10 != 0:
        r = num_b10 % b2
        num_b10 = num_b10 // b2
        if r >= 10: 
            s_b2.insert(0, chr( r-10 + ord('A')))
        else :
            s_b2.insert(0, str(r))
    return "".join(s_b2)


def convert_base(b1: int, s: str, b2: int) -> str :
    
    #symb_int ={"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    n = len(s)


    if b1 == 10 : 
        return convert_from_b10(s, b2)

    num_b10 = 0
    for i in range(n): 
        if s[i].isnumeric():
            num_b10 += int(s[i]) * b1**(n - 1 - i)
        else :
            num_b10 += ( 10 + ord(s[i]) - ord('A') ) * b1**(n - 1 -i)
    
    if b2 == 10 : 
        return num_b10
    
    return convert_from_b10(str(num_b10), b2)

print(convert_from_b10('666', 16))
print(convert_base(8, "1232", 16))