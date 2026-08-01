class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def is_valid(para):
            if para[0] == ')' or para[-1] == '(':
                return False
            o_count = 0
            for i in para:
                if i == '(':
                    o_count += 1
                else:
                    if o_count == 0:
                        return False
                    o_count -= 1
            return o_count == 0
        ret = []
        def paranthesis(wor):
            lis = ['(', ')']
            if len(wor) >= 2*n:
                ret.append(wor)
                return
            for i in lis:
                paranthesis(wor + i)
        paranthesis('')
        ret = list(filter(is_valid, ret))
        return ret

