class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        sandwich = 0
        rotate = 0

        while queue and rotate < len(queue):
            if queue[0] == sandwiches[sandwich]:
                queue.popleft()
                sandwich += 1
                rotate = 0
            else:
                student = queue.popleft()
                queue.append(student)
                rotate += 1
        return len(queue)