class Solution:
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        prev_ch = None

        for ch in s:
            condition1 = (ch ==")" and prev_ch =="(")
            condition2 = (ch =="]" and prev_ch =="[")
            condition3 = (ch =="}" and prev_ch =="{")            
            print(ch)
            if condition1 or condition2 or condition3:
                stack.pop()
                if stack:
                    prev_ch = stack[-1]
                else:
                    prev_ch = None
            else:
                prev_ch = ch
                stack.append(ch)
        print(stack)
        if stack:
            return False
        else:
            return  True        