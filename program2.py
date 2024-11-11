def decode_message(s: str, p: str) -> bool:
    memo = {}
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == len(s) and j == len(p):
            return True
        if j == len(p):
            return False
        match = (i < len(s) and (p[j] == s[i] or p[j] == '?'))
        if p[j] == '*':
            memo[(i, j)] = dp(i, j + 1) or (i < len(s) and dp(i + 1, j))
            return memo[(i, j)]
        if match:
            memo[(i, j)] = dp(i + 1, j + 1)
            return memo[(i, j)]
        memo[(i, j)] = False
        return False
    return dp(0, 0)
