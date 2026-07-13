from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        l = []

        for num in nums:
            d[num] += 1

        for i in range(k):
            max = 0
            mval = 0
            for k, v in d.items():
                if v > max and k not in l:
                    max = v
                    mval = k
            l.append(mval)
        return l
            