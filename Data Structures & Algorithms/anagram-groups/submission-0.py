class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list=[]
        d={}
        for i in strs:
            sorted_list.append("".join(sorted(i)))
        for i in range(0,len(sorted_list)):
            word=sorted_list[i]
            if word in d:
                d[word].append(strs[i])
            else:
                d[word] = [strs[i]]
        ans=[]
        for value in d.values():
            ans.append(value)
        return ans