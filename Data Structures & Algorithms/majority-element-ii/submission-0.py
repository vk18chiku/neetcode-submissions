from collections import Counter
import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)

        dic=Counter(nums)

        return [x for x,count in dic.items() if count>n/3]




        