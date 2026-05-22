class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d={}
        ans=[]

        for i in nums:
            d[i]=nums.count(i)

        d=dict(sorted(d.items(),reverse=True,key=lambda item:item[1]))
        for i in range(0,k):
            ans.append(list(d.keys())[i])
        return ans


        