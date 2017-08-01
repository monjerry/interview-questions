# Return a boolean staging if a string with parenthesis is balanced. (For every "(" there is a ")")

def balancedParentheshis(string):
    # We will just iterate one time through the string and add all ( to a stack
    stack = []
    for character in string:
        if character == '(':
            stack.append(character)
        elif character == ')':
            # If we have "(" in our stack just pop them, else return False
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    return len(stack) == 0

print 'hello(adios()) is {}'.format(balancedParentheshis('hello(adios())'))
print 'hello(adios)) is {}'.format(balancedParentheshis('hello(adios))'))
