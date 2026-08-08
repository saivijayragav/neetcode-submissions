class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ret = set()
        visited = set()
        def dfs(i, s, arr):
            if s == target:
                ret.add(arr)
                return
            if i >= len(candidates) or s > target or (i, s, arr) in visited:
                return
            visited.add((i, s, arr))
            for j in range(i, len(candidates)):
                dfs(j+1, s+candidates[j], arr + tuple([candidates[j]]))
        dfs(0, 0, tuple())
        return list(map(list, ret))