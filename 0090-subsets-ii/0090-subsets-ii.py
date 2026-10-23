class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result=[[]]
        for num in nums:
            for subset in result[:]:
                new_subset=subset+[num]
                if new_subset not in result:
                    result.append(new_subset)
        return result