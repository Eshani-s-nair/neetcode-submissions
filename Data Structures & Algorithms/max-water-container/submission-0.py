class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=[]
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                a=min(heights[i],heights[j])*(j-i)
                area.append(a)
        return max(area)


        