class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans=0
        l=[]
        for i in operations:
            if i not  in "+DC":
                l.append(int(i))
            elif i=="+":
                l.append(l[-1]+l[-2])
            elif i=="C":
                l.remove(l[-1])
            else:
                l.append(2*(l[-1]))
        return sum(l)



        
        