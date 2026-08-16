class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = ['{', '[', '(']
        close = ['}', ']', ')']
        for i in s:
            if i in opens:
                stack.append(i)
            if i == '}':
                if stack and stack[-1] == '{':
                    stack.pop(-1)
                    continue
                else:
                    return False
            if i == ']':
                if stack and stack[-1] == '[':
                    stack.pop(-1)
                    continue
                else:
                    return False
            if i == ')':
                if stack and stack[-1] == '(':
                    stack.pop(-1)
                    continue
                else:
                    return False

        if not (stack):
            return True
        else:
            return False