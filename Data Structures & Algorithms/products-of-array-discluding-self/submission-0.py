class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Answer array
        ans = [1] * n

        # Step 1: Store left product
        prefix = 1

        for i in range(n):
            ans[i] = prefix
            prefix = prefix * nums[i]

        # Step 2: Multiply with right product
        suffix = 1

        for i in range(n - 1, -1, -1):
            ans[i] = ans[i] * suffix
            suffix = suffix * nums[i]

        return ans

