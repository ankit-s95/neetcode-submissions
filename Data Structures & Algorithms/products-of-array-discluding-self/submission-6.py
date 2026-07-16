class Solution:
    def productList(self, nlist: List[int]) -> int:
        product = 1
        for i in nlist:
            product *= i
        return product


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = []
        for i, num in enumerate(nums):
            prod.append(self.productList(nums[:i]) * self.productList(nums[i + 1:]))
        return prod