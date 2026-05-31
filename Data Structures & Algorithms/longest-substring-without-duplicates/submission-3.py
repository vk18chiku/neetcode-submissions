class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        d={}

        high=0
        low=0

        ans=0

        for high in range(0,len(s)):

            d[s[high]]=d.get(s[high],0)+1

            while d[s[high]]>1:
                d[s[low]]-=1

                if d[s[low]]==0:
                    del d[s[low]]

                low=low+1 
            length=high-low+1
            ans=max(ans,length)
        return ans

        