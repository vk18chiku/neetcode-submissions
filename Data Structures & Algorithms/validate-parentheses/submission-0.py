class Solution:
    def isValid(self, s: str) -> bool:

        l = []

        for i in range(0, len(s)):

            if s[i] in "([{":
                l.append(s[i])

            elif s[i] == ")" and len(l) > 0 and l[-1] == "(":
                l.pop()

            elif s[i] == "}" and len(l) > 0 and l[-1] == "{":
                l.pop()

            elif s[i] == "]" and len(l) > 0 and l[-1] == "[":
                l.pop()

            else:
                return False

        if len(l) == 0:
            return True
        else:
            return False