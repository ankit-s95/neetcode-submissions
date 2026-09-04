class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        a = 0
        heapq.heapify(nums)
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        return nums[0]