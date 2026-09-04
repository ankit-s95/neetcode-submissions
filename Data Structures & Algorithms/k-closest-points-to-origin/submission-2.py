import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mins = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            mins.append([dist, x, y])
        
        heapq.heapify(mins)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(mins)
            res.append([x, y])
            k -= 1
        
        return res