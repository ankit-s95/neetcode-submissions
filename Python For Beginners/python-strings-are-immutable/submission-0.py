def remove_fourth_character(word: str) -> str:
    b4 = word[:3]
    a4 = word[4:]
    return b4 + a4


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
