class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        n = len(nums)
        nums.sort()
        res = []

        for k in range(n-2):
            if(k > 0 and nums[k] == nums[k-1]):
                continue

            left, right = k+1, n-1

            while(left < right):
                total = nums[k] + nums[left] + nums[right]
                
                if (total > 0):
                    right -= 1
                elif (total < 0):
                    left += 1
                else:
                    res.append([nums[k], nums[left], nums[right]])

                    left += 1 
                    while(left < right and nums[left-1] == nums[left]):
                        left += 1

        return res 
        