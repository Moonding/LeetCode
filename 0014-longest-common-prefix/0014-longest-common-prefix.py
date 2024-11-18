class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = 200
        min_len_str = ""
        for str in strs:
            str_len =len(str)
            if str_len <= min_len:
                min_len = str_len
                min_len_str = str


        for i,ch in enumerate(min_len_str):
            for str in strs:
                if str[i] !=ch:
                    return min_len_str[:i]

        return min_len_str


        

