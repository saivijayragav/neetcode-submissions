class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        sta = [(0,0)] * len(temperatures)
        for i in range(len(temperatures)):
            temp = temperatures[i]
            while sta and temp > sta[-1][0]:
                j = sta[-1][1]
                ret[j] = i - j
                sta.pop()
            sta.append((temp, i))

        return ret