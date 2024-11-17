class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0:
            return False
        elif x==0:
            return True
        else:
            strx=str(x)
            len_strx=len(strx)
            count = int(len(strx)/2)
            for i in range(count):
                if strx[i] != strx[len_strx-i-1]:
                    return False
            return True