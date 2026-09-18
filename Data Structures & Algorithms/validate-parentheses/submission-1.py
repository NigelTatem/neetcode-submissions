class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {')':'(', ']':'[', '}':'{'}
        paren_stack = []

        for paren in s:
            if paren in paren_map.keys():
                if not paren_stack:
                    return False
                if paren_stack[-1] != paren_map[paren]:
                    return False
                paren_stack.pop()
            else:
                paren_stack.append(paren)
        
        return len(paren_stack) == 0
                