class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parents = [i for i in range(len(points))]
        def findParent(a):
            if parents[a] != a:
                return findParent(parents[a])
            return parents[a]

        joints = []
        for i, (k, v) in enumerate(points):
            for j, (k1, v1) in enumerate(points):
                if i == j:
                    continue
                heapq.heappush(joints, (abs(k1-k)+abs(v1-v), i, j))
        
        ret = 0
        while joints:
            d, a, b = heapq.heappop(joints)
            p1 = findParent(a)
            p2 = findParent(b)
            if p1 == p2:
                continue
            if p1 != p2:
                parents[p2] = p1
                ret += d
        return ret
