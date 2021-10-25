#Prob 2 : Maximal Profit/Difference 
#Faut garder l'ordre 

from typing import List


#We assume len >= 2 
def max_profit(shares: List[int]):
    max_profit = shares[1] - shares[0] #
    min_num = shares[0]

    for i in range(1, len(shares)):
        if max_profit < shares[i] - min_num : #index(min_num) is always < i
            max_profit = shares[i] - min_num
        if min_num > shares[i] :
            min_num = shares[i]
    
    return max_profit
