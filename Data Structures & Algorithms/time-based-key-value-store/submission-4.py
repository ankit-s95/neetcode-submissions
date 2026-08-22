class TimeMap:

    def __init__(self):
        self.hMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hMap:
            self.hMap[key] = []
        self.hMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        lis = self.hMap.get(key, [])
        l = 0
        r = len(lis) - 1
        res = ""
        while l <= r:
            n = (l + r) // 2
            if lis[n][1] <= timestamp:
                res = lis[n][0]
                l = n + 1
            else:
                r = n - 1
        return res