# Lets use the babylonian method. Meaning we use this Formula square = (square + n/squqre)/2)
error_limit = 0.000001
def square_root(n):
    square = n/2.0

    while abs((square * square) - n) > error_limit:
        square = (square + (n / square)) / 2.0
        print square
    return square

print square_root(11.343)
