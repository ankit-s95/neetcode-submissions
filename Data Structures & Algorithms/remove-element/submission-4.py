class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nos = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[nos] = nums[i]
                nos+= 1
        return nos
            