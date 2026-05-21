class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}

        for i in range(0,len(nums)):
            num=target-nums[i]
            if num in d:
                return([d[num], i])
            d[nums[i]] = i


        