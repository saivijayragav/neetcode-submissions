class Solution:
    def compress(self, chars: List[str]) -> int:
        ret = 0
        i = 0
        a = 0
        while i < len(chars):
            r = i
            while r < len(chars)-1 and chars[r+1] == chars[r]:
                r += 1
            if r - i != 0:
                to = chars[i] + str(r-i+1)
                for j in range(len(to)):
                    chars[a] = to[j]
                    ret += 1
                    a += 1
            else:
                chars[a] = chars[i]
                ret += 1
                a += 1
            i = r+1
        return ret
            