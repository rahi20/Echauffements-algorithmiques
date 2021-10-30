# EOPI - Prob 2 : Interconvert Strings And Integers 
# We assume all the chars in string are numeric and the ints are in base 10 


def to_string(num : int) -> str:
    sign = num // abs(num)
    
    s = []
    while num != 0: 
        d = num % 10
        num = num // 10
        s.insert(0, chr( 48 + d )) #48 is the ascii code of 0, ord("0") works too

    return "".join(s)


def to_int(s : str) -> int:

    n = len(s)
    num = 0
    for i in range(n):
        num += ( ord(s[n - 1 - i]) - 48 ) * 10**i # or ord(48)

    return num


print(to_string(123))
print(to_int("123"))