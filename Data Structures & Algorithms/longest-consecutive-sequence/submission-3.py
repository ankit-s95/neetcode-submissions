
class Solution:

    def maxVal(self, l: List[int]) -> int:
        max = 0
        for val in l:
            if val > max:
                max = val
        return max



    def longestConsecutive(self, nums: List[int]) -> int:
        snums = set(nums)
        cons = 0
        for num in nums:
            if num - 1 not in snums:
                l = 0
                while num + l in snums:
                    l += 1
                cons = max(l, cons)
        return cons
            