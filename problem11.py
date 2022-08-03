class Solution:
    def maxArea(self, height) -> int:
        maxarea = 0
        left = 0
        right = len(height) - 1
        while(left < right):
            area = (right-left)*min(height[left],height[right])
            if(area > maxarea):
                maxarea = area
            if(height[left]<height[right]):
                left += 1
            else:
                right -= 1