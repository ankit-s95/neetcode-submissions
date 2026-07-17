class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = []
        for i, nums in enumerate(numbers):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]