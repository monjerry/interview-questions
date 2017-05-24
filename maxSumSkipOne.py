def maxSumSkipOne(arr):
    if len(arr) == 1:
        return [0]
    opts = [0] * (len(arr) + 2)
    i = len(arr) - 1
    while i >= 0:
        opts[i] = arr[i] + max(opts[i+1], opts[i+2])
        print opts
        i-=1
    return max(opts[0], opts[1])


def maxSumSkipOne2(arr):
    skip = 0
    count = 0
    newCount = 0
    n = len(arr)
    if n == 1:
        return arr[0]
    for i in arr:
        newCount = count + i
        if newCount >= skip:
            count = newCount
            skip = newCount
        else:
            count = skip
            skip = newCount
        print 'i {} count {} skip {}'.format(i, count, skip)
    return count
arr = [5, 5, -12, -1, -1, -6, 5, 5]

print maxSumSkipOne(arr)
print maxSumSkipOne2(arr)
