from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dict=Counter(nums)

        return [x for x ,count in dict.most_common(k)]

        


        