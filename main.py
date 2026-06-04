# Built-in imports

def is_palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])

def generate_permutations(s: str) -> list[str]:
    s_len = len(s)
    if s_len == 0:
        return [""]
    if s_len == 1:
        return [s]
    perms = []
    for i, c in enumerate(s):
        before_c = s[:i]
        after_c = ""
        if i < s_len - 1:
            after_c = s[i+1:]
        s_without_c = before_c + after_c
        perms_partial = generate_permutations(s_without_c)
        for partial_perm in perms_partial:
            perms.append(partial_perm + c)

    return perms

def num_paths(m: int, n: int) -> int:
    if m <= 0 or n <= 0:
        return 1
    return num_paths(m-1, n) + num_paths(m, n-1)

print(generate_permutations("abc"))

print(num_paths(2, 2))
