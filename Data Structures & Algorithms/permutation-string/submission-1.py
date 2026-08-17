class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        n = len(s1)
        sortsub = sorted(s1)
        for l in range(len(s2)):
            sortwin = sorted(s2[l: l + n])
            if sortwin == sortsub:
                return True
        return False