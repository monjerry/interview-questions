def firstNonRepeating(string):
    counts = {}
    index = -1
    for char in string:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    for x in counts:
        if counts[x] == 1:
            return x
    return '_'
