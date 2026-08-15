class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        i = 0
        while i < len(chars):
            r = i
            while r < len(chars)-1 and chars[r+1] == chars[r]:
                r += 1
            if r - i == 0:
                s += chars[i]
            else:
                s += chars[i]
                s += str(r-i+1)
            i = r+1
        chars[:] = list(s)
        return len(s)
            