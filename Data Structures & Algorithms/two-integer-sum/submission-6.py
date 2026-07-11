class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hmap:
                return [hmap[difference], i]
            else:
                hmap[nums[i]] = i