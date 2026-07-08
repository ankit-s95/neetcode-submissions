def concatenate(s1: str, s2: str) -> str:
    join = s1 + s2
    if len(join) > 10:
        return "Too long!"
    else:
        return join




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
