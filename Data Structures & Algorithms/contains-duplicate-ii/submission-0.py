from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        d = {}

        for i in range(0, len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
            else:
                val = i - d[nums[i]]

                if val <= k:
                    return True

                d[nums[i]] = i

        return False





        