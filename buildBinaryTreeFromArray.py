def buildBinaryTree(arr):
    n = len(arr)
    if n == 0:
        return None
    if n == 1:
        return {'val': arr[0], 'left': None, 'right': None}
    mid = n/2
    root = {'val': arr[mid], 'left': buildBinaryTree(arr[:mid]), 'right':
            buildBinaryTree(arr[mid+1:])}
    return root

arr = sorted([5,2,7,9,3,2,4,0])
print arr
print buildBinaryTree(arr)
    
