class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = 0
        end = 0
        ans = 0
        count = 0
        seen = set()

        while end < len(s):

            if s[end] not in seen:
                seen.add(s[end])
                count = count + 1
                end = end + 1

            else:
                seen.remove(s[start])
                start = start + 1
                count = count - 1

            ans = max(ans, count)

        return ans
            
        
        

        