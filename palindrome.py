from collections import deque

stack = deque()

palindrome = "abccba"


def check_palindrome(string: str):
    # s2 = string[:len(string) // 2]
    # s3 = string[len(string) // 2:]
    # # for letter in
    # if s2 == s3[::-1]:
    #     return True
    res = True
    for order, character in enumerate(string):
        if not res:
            return res
        if order < len(string) / 2:
            stack.append(character)
        else:
            if stack.pop() != character:
                res = False
    return res


wrong_palindrome = "abccab"
print(check_palindrome(palindrome))

print(check_palindrome(wrong_palindrome))
