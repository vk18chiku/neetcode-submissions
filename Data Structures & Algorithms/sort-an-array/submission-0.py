class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        for i in range(0,len(nums)-1):
            mindx=i
            for j in range(i+1,len(nums)):
                if nums[j]<=nums[mindx]:
                    mindx=j 
            nums[i],nums[mindx]=nums[mindx],nums[i]
        return nums