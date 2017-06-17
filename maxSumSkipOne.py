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
    print 'Array is {}'.format(arr)
    for i in arr:
        print '****************************************'
        newCount = count + i
        print 'The current possible count is {} + ({}) = {}'.format(count, i, newCount)
        if newCount >= skip:
            print 'We want to have this number as is bigger than the last skipped'
            count = newCount
            skip = newCount
        else:
            print 'We may not want this number as its decreasing our count'
            count = skip
            skip = newCount
        print 'Current number is {} count {} skip {}'.format(i, count, skip)
    return count
arr = [5, 5, -12, -1, -1, -6, -7]

print maxSumSkipOne(arr)
print maxSumSkipOne2(arr)
