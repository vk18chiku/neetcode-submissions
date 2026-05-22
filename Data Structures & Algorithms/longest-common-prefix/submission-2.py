class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        ans = []

        for i in range(len(strs[0])):
            word = strs[0][i]

            for j in range(1, len(strs)):

                if i >= len(strs[j]) or strs[j][i] != word:
                    return "".join(ans)

            ans.append(word)

        return "".join(ans)
