def nondecreasing(arr):
    opts = [1] * len(arr)
    print 'Array is  {}'.format(arr)
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] > arr[j] and opts[i] < opts[j] + 1:
                opts[i] = opts[j] + 1
            print 'Options = {} for i = {}, j = {}'.format(opts, i, j)
    return max(opts)

arr =[10, 22, 9, 33, 7,8,9, 21, 50]

nondecreasing(arr)

