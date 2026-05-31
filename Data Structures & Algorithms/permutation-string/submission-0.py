class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        low=0
        high=len(s1)-1

        d1={}

        for ch in s1:
            d1[ch] = d1.get(ch, 0) + 1

        while high<len(s2):

            new_s=s2[low:high+1]
            d2={}
            for ch in new_s:
                d2[ch] = d2.get(ch, 0) + 1
            if d2==d1:
                return True 

            low=low+1
            high=high+1 
        return False

        