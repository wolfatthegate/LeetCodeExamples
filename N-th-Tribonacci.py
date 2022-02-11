class Solution:
    def tribonacci(self, n: int) -> int:
        def dp(n):
            if n == 0: 
                return 0
            if n == 1: 
                return 1
            if n == 2: 
                return 1

            if n in memo: 
                return memo[n]
            
            memo[n] = dp(n-3) + dp(n-2) + dp(n-1)
            return memo[n]
        
        memo = {}
        return dp(n)
