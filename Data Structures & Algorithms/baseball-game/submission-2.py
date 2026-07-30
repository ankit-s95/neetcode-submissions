class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for e in operations:
            n = len(record)
            if e == 'C' and n > 0:
                del record[n - 1]
            elif e == 'D' and n > 0:
                record.append((record[n - 1] * 2))
            elif e == '+' and n > 1:
                record.append((record[n - 1] + record[n - 2]))
            else:
                record.append(int(e))
        return sum(record)