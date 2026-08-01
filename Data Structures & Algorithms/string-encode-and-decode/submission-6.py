class Solution:
    def encode(self, strs: List[str]) -> str:
        ret = []
        for i in strs:
            ret.append(str(len(i))+'#'+i)
        return ''.join(ret)
    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i<len(s):
            n = ''
            while s[i] != '#':
                n += s[i]
                i += 1
            print(n)
            ret.append(s[i+1:i+1+int(n)])
            i += int(n) + 1
        return ret
