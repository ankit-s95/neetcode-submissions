class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxv = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            if maxv < min(heights[l], heights[r]) * (r - l):
                maxv = min(heights[l], heights[r]) * (r - l)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxv
