class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def union(self, node1, node2):
        node1_rep = self.find(node1)
        node2_rep = self.find(node2)
        self.parent[node1_rep] = node2_rep

    def find(self, node):
        if node == self.parent[node]:
            return node
        return self.find(self.parent[node])
