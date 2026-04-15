class Solution:
    def isValid(self, s: str) -> bool:
        valid = { ']':'[','}':'{', ')':'(',  }
        stack = []

        for c in s:
            if c in valid:
                if stack and stack[-1] == valid[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
        