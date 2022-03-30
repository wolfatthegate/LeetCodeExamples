/* This is a top-down implementation with Recursive function

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn. 

*/

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
