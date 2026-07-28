class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)
        n= len(snums)
        l = []
        for i in range(0, n - 2):
            if snums[i] > 0:
                break
            if snums[i] != snums[i - 1] or i == 0:

                j = i + 1
                k = n - 1
                while j < k:
                    if -snums[i] == snums[j] + snums[k]:
                        l.append([snums[i], snums[j], snums[k]])
                        k -= 1
                        j += 1
                        while j < k and snums[k] == snums[k + 1]:
                            k -= 1
                        while j < k and snums[j] == snums[j - 1]:
                            j += 1
                    elif -snums[i] < snums[j] + snums[k]:
                        k -= 1
                    else:
                        j += 1
                    #ii.append(snums[i])
        return l