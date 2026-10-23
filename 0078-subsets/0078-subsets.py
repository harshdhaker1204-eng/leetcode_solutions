class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result=[[]]
        for num in nums:
            for subset in result[:]:
                result.append(subset+[num])
        return result