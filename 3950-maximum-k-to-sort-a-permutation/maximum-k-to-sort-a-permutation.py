class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        if nums==sorted(nums):
            return 0
        k=-1
        for i in range(len(nums)):
            if nums[i]!=i:
                k&=nums[i]
        return k