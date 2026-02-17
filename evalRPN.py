class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        op = ("+", "-", "*", "/")
        for i in tokens:
            if i not in op:
                stack.append(int(i))
            if i in op:
                b= stack.pop()
                a= stack.pop()
                if i == '+':
                    stack.append(a + b)
                elif i == '-':
                    stack.append(a - b)
                elif i == '*':
                    stack.append(a * b)
                elif i == '/':
                    stack.append(int(a / b))

        return stack[0]

                
        
