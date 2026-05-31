class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        low=0

        high=0

        ans= 0

        for high in range(0,len(prices)):
            diff=prices[high]-prices[low]

            if diff<0:
                low=high
            ans=max(diff,ans)

        return ans

        


        