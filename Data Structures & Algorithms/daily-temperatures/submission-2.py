class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        sta = [(0,0)] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while sta and temp > sta[-1][0]:
                t, j = sta.pop()
                ret[j] = i - j
            sta.append((temp, i))

        return ret