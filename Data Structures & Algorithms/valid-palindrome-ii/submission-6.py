class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalindrome(left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left=left+1
                right=right-1
            return True 

        start=0
        end=len(s)-1

        while start<end:
            if s[start]!=s[end]:
                return (
                    ispalindrome(start+1,end) or
                    ispalindrome(start,end-1)
                ) 

            start=start+1
            end=end-1 
        return True
