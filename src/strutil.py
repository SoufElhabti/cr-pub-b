def reverse(s):
    return s[::-1]


def count_vowels(s):
    n = 0
    for ch in s:
        if ch in "aeiou":
            n += 1
    return n
