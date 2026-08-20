class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        targrow = 1
        if r == 0:
            if target in matrix[0]:
                return True
            else: return False
        while l <= r:
            n = (l + r) // 2
            if matrix[n][0] == target:
                return True
            elif matrix[n][0] > target:
                r = n - 1
            else:
                l = n + 1
        if l > 0:
            targrow = l - 1
        else:
            return False

        lef = 0
        rig = len(matrix[0]) - 1
        while lef <= rig:
            n = (lef + rig) // 2
            if matrix[targrow][n] == target:
                return True
            elif matrix[targrow][n] < target:
                lef = n + 1
            else:
                rig = n - 1
        return False