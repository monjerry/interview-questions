def rotateMatrix(a):
    n = len(a)
    b = []
    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(0)
        b.append(tmp)
            
    for i in range(n):
        for j in range(n):
            b[i][j] = a[n - j - 1][i]
    return b

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print rotateMatrix(a)
