def calculateSpan(price, S):
    printArray(price)     
    n = len(price)
    # Create a stack and push index of fist element to it
    st = [] 
    st.append(0)
 
    # Span value of first element is always 1
    S[0] = 1
 
    # Calculate span values for rest of the elements
    for i in range(1, n):
         
        # Pop elements from stack whlie stack is not
        # empty and top of stack is smaller than price[i]
        while( len(st) > 0 and price[st[-1]] <= price[i]):
            st.pop()
 
        # If stack becomes empty, then price[i] is greater
        # than all elements on left of it, i.e. price[0],
        # price[1], ..price[i-1]. Else the price[i]  is
        # greater than elements after top of stack
        S[i] = i+1 if len(st) <= 0 else (i - st[-1])
 
        # Push this element to stack
        st.append(i)
 
 
# A utility function to print elements of array
def printArray(arr):
    print '['+ ', '.join(map(str, arr)) + ']'
 
 
# Driver program to test above function
price = [10, 4, 5, 90, 120, 80]
S = [0 for i in range(len(price)+1)]
 
# Fill the span values in array S[]
calculateSpan(price, S)
 
# Print the calculated span values
printArray(S)
