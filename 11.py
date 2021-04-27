class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        low,high = 0,len(height)-1
        area = 0
        while low+1 <= high:
            area = max(area,min(height[low],height[high])*(high-low))
            
            if height[low] < height[high]:
                #move left
                low += 1
            else:
                #move right
                high -= 1
                
        return area
