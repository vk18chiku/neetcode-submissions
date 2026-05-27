class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=''

        left=0
        right=0

        while left<len(word1) and right<len(word2):
            ans=ans+word1[left]
            ans=ans+word2[right]

            left=left+1
            right=right+1 

        while left<len(word1):
            ans=ans+word1[left]
            left=left+1

        while right<len(word2):
            ans=ans+word2[right]
            right=right+1
        return ans

        