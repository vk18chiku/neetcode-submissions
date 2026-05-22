class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s=set(nums)

        d={}

        for i in s:
            d[i]=nums.count(i)
        return(max(d, key=d.get))