def sumInArray(array, suma):
    hashDict = {}
    for item in array:
        # If the item is in the array it means there is a number that will
        # up to the sum
        if item in hashDict:
            return True
        else:
            # Set the key to be the number that needs to be in the array to add
            # up to the sum
            hashDict[suma - item] = True
    return False


array = [3, 5, 2,7 ,3]
print sumInArray(array, 6)
print sumInArray(array, 100)
