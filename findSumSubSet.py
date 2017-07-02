def printMatrix(arr):
    for row in arr:
        print row


def findSubSetSum(arr, sumToFind):
    opts = []
    for x in arr:
        tmp = []
        for i in range(sumToFind+1):
            tmp.append(None)
        tmp[0] = True
        opts.append(tmp)
    print 'We will start with this matrix'
    printMatrix(opts)
    for i in range(len(arr)):
        for j in range(1, sumToFind + 1):
            if arr[i] > j:
                if i != 0:
                    opts[i][j] = opts[i-1][j]
                else:
                    opts[i][j] = False
            elif arr[i] == j:
                opts[i][j] = True
            else:
                if i != 0:
                    opts[i][j] = opts[i-1][j-arr[i]]
                else:
                    opts[i][j] = False
    print 'Final matrix'
    printMatrix(opts)
    if opts[len(arr) -1][sumToFind]:
        res = []
        j = sumToFind
        i = len(arr) - 1
        while (True):
            if not opts[i-1][j]:
                res.append(arr[i])
                j = j - arr[i]
            else:
                i-=1
            if j == 0 or i == 0:
                res.append(arr[i])
                break
        return True, res
    else:
        return False, []

arr = [1, 2, 3, 4, 5, 21,23, 44]
suma = 9

print findSubSetSum(arr, suma)

