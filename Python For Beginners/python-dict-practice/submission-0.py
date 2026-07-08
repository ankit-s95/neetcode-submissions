from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    num_char = {}
    for char in word:
        count = 0
        for c in word:
            if char == c:
                count += 1
        num_char[char] = count
    return num_char



# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
