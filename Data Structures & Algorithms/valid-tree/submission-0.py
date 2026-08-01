class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        parent = [i for i in range(n)]
        def findParent(node):
            if parent[node] == node:
                return node
            return findParent(parent[node])
        
        for n1, n2 in edges:
            p1 = findParent(n1)
            p2 = findParent(n2)
            if p1 == p2:
                return False
            parent[p1] = p2
        return True