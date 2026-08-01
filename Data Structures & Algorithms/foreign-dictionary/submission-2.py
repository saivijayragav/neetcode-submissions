from collections import defaultdict, deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        incoming_edge = defaultdict(int)
        edges = defaultdict(list)
        for i in range(len(words)):
            w1 = words[i]
            for j in range(i+1, len(words)):
                w2 = words[j]
                ind = 0
                while ind < len(w1):
                    if ind >= len(w2):
                        return ""
                    if w1[ind] != w2[ind]:
                        incoming_edge[w2[ind]] += 1
                        edges[w1[ind]].append(w2[ind])
                        break
                    ind += 1
        
        chars = list(set("".join(words)))
        q = deque()
        for ch in chars:
            if incoming_edge[ch] == 0:
                q.append(ch)
        ret = []
        while q:
            ch = q.popleft()
            ret.append(ch)
            for char in edges[ch]:
                incoming_edge[char] -= 1
                if incoming_edge[char] == 0:
                    q.append(char)
        if len(ret) != len(chars):
            return ""
        return "".join(ret)