class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        st=set(nums)

        if len(st)!=len(nums):
            return True 
        else:
            return False