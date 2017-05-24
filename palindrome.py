# palindrome with recursion although it may break for really long ones
def palindrome(s, start, end):
    if len(s) == 1 or start == end:
        return 1
    if s[start] == s[end] and start + 1 == end:
        return 2
    elif s[start] == s[end]:
        return palindrome(s, start + 1, end -1) + 2
    else:
        return max(palindrome(s, start + 1, end), palindrome(s, start, end -1))


# Palindrome with dynamic programming
def palindrome2(s):
    matrix = []
    n = len(s)
    for i in range(len(s)):
        matrix.append([0 for x in range(n)])
    for i in range(n):
        matrix[i][i] = 1
    for pl in range(2, n+1):
        skip = pl - 1
        i = 0
        j = i + skip
        while True:
            j = i + skip
            if j >= n:
                break
            if s[i] == s[j] and pl == 2:
                matrix[i][j] = 2
            elif pl == 2:
                matrix[i][j] = 1
            elif s[i] != s[j]:
                matrix[i][j] = max(matrix[i+1][j], matrix[i][j-1])
            else:
                matrix[i][j] = 2 + matrix[i+1][j-1]
            i+=1
    return matrix[0][n-1]

# Can be either an array of ints or a string
st = [1, 1, 4, 1]
print palindrome(st, 0, len(st)-1)
print palindrome2(st)
