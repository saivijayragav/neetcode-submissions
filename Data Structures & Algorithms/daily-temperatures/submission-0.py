class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        for i in range(len(temperatures)):
            temp = temperatures[i]
            for j in range(i+1, len(temperatures)):
                if temp < temperatures[j]:
                    ret[i] = j-i
                    break
        return ret