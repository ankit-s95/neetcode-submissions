class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numset = set()

        for i in nums:
            n = len(numset)
            numset.add(i)
            if len(numset) == n:
                return i