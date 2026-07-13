class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = "".join(char for char in s if char.isalnum()).lower()
        print(s1)
        for i in range(len(s1)):
            if s1[i] != s1[len(s1) - i - 1]:
                return False
        return True