def nondecreasing(arr):
    opts = [1] * len(arr)
    print arr
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] > arr[j] and opts[i] < opts[j] + 1:
                opts[i] = opts[j] + 1
    print opts
    return max(opts)

arr =[10, 22, 9, 33, 1, 2, 3 ,4,5,6,7,8,9, 21, 50, 41, 60]

print nondecreasing(arr)

