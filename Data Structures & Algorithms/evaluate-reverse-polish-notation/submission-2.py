class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        operators = ['+', '-', '*', '/']
        dict_oper = {
            '+':lambda a,b:a+b,
            '-':lambda a,b:a-b,
            '*':lambda a,b:a*b,
            '/':lambda a,b:a/b
        }
        for i in tokens:
            if i not in operators:
                operands.append(i)
            else:
                operation = dict_oper[i](int(operands[-2]), int(operands[-1]))
                operands.pop()
                operands.pop()
                operands.append(operation)
        return round(int(operands[0]))
                
        