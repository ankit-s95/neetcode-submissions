class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        result = r
        while l <= r:
            time = 0
            n = (l + r) // 2
            for i in piles:
                time += math.ceil(i / n)
            if time <= h:
                result = min(result, n)
                r = n - 1
            else:
                l = n + 1
        return result
