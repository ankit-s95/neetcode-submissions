class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        wuns = 0
        zeros = 0
        for i in students:
            if i == 0:
                zeros += 1
            else:
                wuns += 1
        while students:
            if sandwiches[0] == 0 and zeros == 0:
                break
            elif sandwiches[0] == 1 and wuns == 0:
                break
            a = students.pop(0)
            if a != sandwiches[0]:
                students.append(a)
            else:
                sandwiches.pop(0)
                if a == 0:
                    zeros -= 1
                else:
                    wuns -= 1
        return len(students)
            