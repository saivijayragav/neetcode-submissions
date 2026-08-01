class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        counts = Counter(senate)
        c = 0
        while counts['R'] != 0 and counts['D'] != 0:
            for i, ch in enumerate(senate):
                if ch == 'R':
                    if c < 0:
                        senate[i] = ''
                        counts['R'] -= 1
                    c += 1
                elif ch == 'D':
                    if c > 0:
                        senate[i] = ''
                        counts['D'] -= 1
                    c -= 1
        if counts['R'] != 0:
            return "Radiant"
        return "Dire"    


        