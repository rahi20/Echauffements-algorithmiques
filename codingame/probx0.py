# Let's consider the following sequence of digits : 1234578910111213...
# where all natural numbers from 1 onwards show up in order 
# Given an intger n, find the nth decimal digit of that sequence
# For example: The 1st digit is 1, the 10th digit is 1 and the 11th digit is 0



#naive 
def get_nth_0(n: int):
    seq = ""
    num = 0
    for i in range(1, n+1):
        num += 1
        seq += str(num)
    print (seq)
    return seq[n-1]


def get_nth(n: int):
    return ""


n = int(input())
print(get_nth_0(n))