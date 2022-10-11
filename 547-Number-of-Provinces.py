class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        numCities = len(isConnected) 
        root = [i for i in range(numCities)]
        rank = [1] * numCities
        
        def find(x): 
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(x, y): 
            rootX = find(x)
            rootY = find(y)
            
            if rootX != rootY:                # ** it is important that we compare  
                if rank[rootX] > rank[rootY]: # rank[rootX] and rank[rootY]; 
                    root[rootY] = rootX       # not rank[x] and rank[y]
                elif rank[rootY] > rank[rootX]:
                    root[rootX] = rootY
                else: 
                    root[rootY] = rootX
                    rank[rootX] += 1
                
        for i in range(numCities): 
            for j in range(i+1,numCities): 
                if isConnected[i][j] == 1: 
                    union(i, j)

        ans = set()
        for i in range(numCities): 
            ans.add(find(i))

        return len(ans)
