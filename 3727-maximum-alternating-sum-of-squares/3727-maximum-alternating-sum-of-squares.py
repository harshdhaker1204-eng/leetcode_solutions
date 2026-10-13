class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sq=sorted(v*v for v in nums)
        k=len(nums)//2
        return sum(sq)-2*sum(sq[:k])