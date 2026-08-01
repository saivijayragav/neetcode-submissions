class Solution:
    def __init__(self):
        self.breaks = []
    def encode(self, strs: List[str]) -> str:
        cur = 0
        for i in strs:
            cur += len(i)
            self.breaks.append(cur)
        return ''.join(strs)
    def decode(self, s: str) -> List[str]:
        ret = []
        cur = 0
        for i in self.breaks:
            ret.append(s[cur:i])
            cur = i
        return ret
