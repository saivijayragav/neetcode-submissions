class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += str(len(s))+"#"+s
        return ret
    def decode(self, s: str) -> List[str]:
        i = 0
        ret = []
        while i < len(s):
            n = ''
            while i < len(s) and s[i] != '#':
                n += s[i]
                i += 1
            n = int(n)
            i += 1
            ret.append(s[i:i+n])
            i += n
        return ret