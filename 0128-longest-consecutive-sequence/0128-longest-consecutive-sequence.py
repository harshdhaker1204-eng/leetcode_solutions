class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        arrs=sorted(nums)
        count=1
        ans=1
        for i in range(len(arrs)-1):
            if arrs[i]+1==arrs[i+1]:
                count+=1
            elif arrs[i]==arrs[i+1]:
                continue
            else:
                count=1
            ans=max(count,ans)
        return ans