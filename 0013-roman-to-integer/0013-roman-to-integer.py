class Solution:
    def romanToInt(self, s: str) -> int:
        two_symbol_val = {
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900

        }
        one_symbol_val = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        s_len = len(s)
        total = 0
        i = 0
        while i < s_len:
            print(total)
            first = s[i]
            if i<s_len-1:
                second = s[i+1]
                two_val = two_symbol_val.get(first+second,None)
                if two_val :
                    total += two_val
                    i+=2
                    continue
            
            first_val =one_symbol_val.get(first,None)
            total += first_val
            i+=1
            


        return total