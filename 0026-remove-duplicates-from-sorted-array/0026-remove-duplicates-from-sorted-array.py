class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s1=set([])
        i = 0
        end = len(nums)
        while i< end:
            val = nums[i]
            if val not in s1:
                s1.add(val)
                i+=1
            else:
                nums.pop(i)
                end-=1

        return len(nums)