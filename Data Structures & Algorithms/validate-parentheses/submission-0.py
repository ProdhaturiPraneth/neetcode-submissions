class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Map each closing bracket to its required opening counterpart
        close_to_open = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in close_to_open:
                # If we see a closing bracket, ensure stack is non-empty 
                # and top of stack matches the needed opening bracket
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()  # Remove matched open bracket
                else:
                    return False
            else:
                # Push opening brackets onto the stack
                stack.append(char)

        # Return True only if all opening brackets were popped
        return len(stack) == 0