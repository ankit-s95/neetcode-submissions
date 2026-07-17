class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1 = 0
        current = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
            else:
                if current > max1:
                        max1 = current
                current = 0
            if i == len(nums) - 1:
                if current > max1:
                        max1 = current
                current = 0
        return max1
