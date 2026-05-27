class Solution:
    def maxArea(self, heights: List[int]) -> int:

        start=0
        end=len(heights)-1

        max_area=0

        while start<end:

            min_heights=min(heights[start],heights[end])

            width=end-start

            area=width*(min_heights)

            max_area=max(area,max_area)

            if heights[start]<heights[end]:
                start=start+1 
            else:
                end=end-1 
        return max_area

        