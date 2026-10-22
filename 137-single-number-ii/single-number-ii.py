class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        hash_map={}
        for num in nums:
            hash_map[num]=hash_map.get(num,0)+1
        for num,count in hash_map.items():
            if count==1:
                return num