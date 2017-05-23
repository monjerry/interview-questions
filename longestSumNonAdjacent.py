def countMaxSkip(arr):
    include = 0
    print arr
    exclude = 0
    for item in arr:
        if include > exclude:
            new_exclude = include
        else:
            new_exclude = exclude
        include = exclude + item
        exclude = new_exclude
        print 'include {} exclude {}'.format(include, exclude)
    return max(exclude, include)


array = [1, 4, 5, 1, 10, 17, 17]

print countMaxSkip(array)
