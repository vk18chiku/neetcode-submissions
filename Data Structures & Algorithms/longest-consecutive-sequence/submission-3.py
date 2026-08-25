class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums.sort()

        cnt=1
        ans=1

        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                cnt=cnt+1 
            elif nums[i]==nums[i-1]:
                continue 
            else:
                cnt=1 

            ans=max(ans,cnt)

        return ans
        