class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit=0
        start=0
        end=1

        while end<len(prices):
            if prices[start]<prices[end]:
                sell=prices[end]-prices[start]
                profit=max(sell,profit)
            else:
                start=end 
            end=end+1

            

        return profit
        


        