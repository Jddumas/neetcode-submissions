class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {')': '(', '}': '{', ']': '[' }
        stack = []

        for char in s:

            # if it in the dict (value) then push (opening)
            if char not in dict1:
                stack.append(char)

            # else its closing
            else:
                if not stack:
                    return False 
                
                closing_char = stack.pop()
                if not dict1[char] == closing_char:
                    return False

        if not stack:
            return True
        else:
            return False
