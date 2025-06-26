class Solution(object):
    def findRedundantConnection(self, edges):
        union_find = Union_Find(len(edges))

        for source, neighbor in edges:
            if not union_find.union(source, neighbor):
                return [source, neighbor]

        return [-1, -1]

class Union_Find(object):
    def __init__(self, size):
        self.parent = list(range(size + 1))
        self.rank = [1] * (size + 1)

    def find(self, element):
        if self.parent[element] != element:
            self.parent[element] = self.find(self.parent[element])

        return self.parent[element]

    def union(self, one, two):
        one_head = self.find(one)
        two_head = self.find(two)

        if one_head == two_head:
            return False
        elif self.rank[one_head] > self.rank[two_head]:
            self.parent[two_head] = one_head
        elif self.rank[one_head] < self.rank[two_head]:
            self.parent[one_head] = two_head
        else:
            self.parent[one_head] = two_head
            self.rank[two_head] += 1
        
        return True


        


            