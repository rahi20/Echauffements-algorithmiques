# Reverse an int

def reverse(num: int) -> int:

    sign = num // abs(num)
    s = 0
    num = abs(num)
    
    while num >= 1: 
        d = num % 10 
        num = num // 10
        s = s*10 + d

    return s*sign

print(reverse(-148))