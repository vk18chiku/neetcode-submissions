class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        low = 0
        high = k - 1

        best_sum = float('inf')
        ans = []

        while high < len(arr):

            sum1 = 0

            for i in range(low, high + 1):
                diff = abs(x - arr[i])
                sum1 += diff

            if sum1 < best_sum:
                best_sum = sum1
                ans = arr[low:high + 1]

            low += 1
            high += 1

        return ans

            

        