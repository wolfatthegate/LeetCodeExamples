class UnionFind: 
    def __init__(self, size): 
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    
    def find(self, x): 
        if x == self.root[x]: 
            return x
        self.root[x] == self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y): 
        rootX = self.root[x]
        rootY = self.root[y]
        
        if rootX != rootY: 
            if self.rank[x] > self.rank[y]: 
                self.root[y] = rootX
            elif self.rank[y] > self.rank[x]: 
                self.root[x] = rootY
            else: 
                self.root[y] = rootX
                self.rank[x] += 1 
      
    def connected(self, x, y): 
        return self.root[x] == self.root[y]
# Test Case
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true
