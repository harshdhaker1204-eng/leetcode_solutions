class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        seen=set(nums)
        num=1
        while num in seen:
            num=num+1
        return num

