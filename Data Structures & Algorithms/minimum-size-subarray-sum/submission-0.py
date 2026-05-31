class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        low=0
        sum=0
        ans=float('inf')

        for high in range(0,len(nums)):
            sum=sum+nums[high]

            while sum >= target:
                ans=min(ans,high-low+1)
                sum=sum-nums[low]
                
                low=low+1

            

        return 0 if ans == float('inf') else ans
        