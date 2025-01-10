def isValid( s: str) -> bool:
    
    if not s:
        return False 
    
    # stack 

    matching = {
        ')': '(', 
        '}': '{', 
        ']': '['}
    stack = []

    for char in s:
        # opening paranthesis
        if char in matching.values(): 
            # will be searching the closing match 
            stack.append(char)

        # closing paranthesis 
        elif char in matching.keys():
            if stack and stack[-1] == matching[char]:
                # matching done 
                stack.pop()
            else:
                return False
        else:
            return False
    # if stack is empty all matching was done
    return not stack 




# result =  isValid( "()" )
# result =  isValid( "()[]{}" )
# result =  isValid( "(]" )
# result =  isValid( "([])" )
# result =  isValid( "]" )
# result =  isValid( "(){}]" )
# result =  isValid( "(){}}{" )
result =  isValid( "({)}" )

print(result)