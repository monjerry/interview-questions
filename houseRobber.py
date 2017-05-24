def robHouse(arr):
    including = 0
    excluding = 0
    for i in range(0, len(arr)):
        new_exclude = max(including, excluding)
        including += arr[i]
        excluding = new_exclude
    return max(excluding, including)

