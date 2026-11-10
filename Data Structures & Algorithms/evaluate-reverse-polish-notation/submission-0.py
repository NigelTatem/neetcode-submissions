from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # maintain two stacks one for operands and one for numbers
        # we collect the operands from left to right and apply them by popping the last to the first element of the queue of numbers to evaluate the expression

        # we evaluate the current total whenever there is an end to operands collected

        stack = []
        
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        
        return stack[0]

