#Easy Prob 13: Roman To Int

class Solution:
    def romanToInt(self, s: str) -> int:
        symb_int = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        sub_inst = {
            'IV' : 4,
            'IX' : 9,
            'XL' : 40,
            'XC' : 90,
            'CD' : 400,
            'CM' : 900
        }
        
        order = 'IVXLCDM'
        n = len(s)
        i = 0

        num = 0
    
        while i < n:
            if i<n-1 and order.index(s[i]) < order.index(s[i+1]):
                num += sub_inst[ s[i]+s[i+1] ]
                i += 2
                continue
            else :
                num += symb_int[s[i]]

            i += 1        
        
        return num

    def int_to_roman(self, num: int) -> str:
        n = 1


sol = Solution()

print(sol.romanToInt('MMMCMXCIX'))