class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {')': '(', '}': '{', ']': '[' }
        stack = []

        for char in s:
            if char not in dict1:
                stack.append(char)

            else:
                if not stack:
                    return False
                
                # check
                closing_char = stack.pop()
                if not dict1[char] == closing_char:
                    return False

        if not stack:
            return True
        return False
