class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            a, b = stones.pop(-1), stones.pop(-1)
            if a == b:
                continue
            else:
                stones.append(abs(a - b))
        if stones:
            return stones[0]
        else:
            return 0
