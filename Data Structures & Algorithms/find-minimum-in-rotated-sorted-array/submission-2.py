class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            n = (l + r) // 2
            if nums[n] > nums[r]:
                l = n + 1
            else:
                r = n
        return nums[l]