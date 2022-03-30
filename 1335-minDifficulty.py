''' 1335. Minimum Difficulty of a Job Schedule 
https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
'''

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        memo = {}
        
        def dp(jobDifficulty, d):
            n = len(jobDifficulty)
            if d == 0 and n ==0: 
                return 0
            if d == 1: 
                return max(jobDifficulty)
            if len(jobDifficulty) < d:
                return -1
            if len(jobDifficulty) == d: 
                return sum(jobDifficulty)
            
            if (n,d) not in memo: 
                mini = sys.maxsize - 1

                for i in range(1, len(jobDifficulty)-d+2, 1):

                    mini = min(mini, max(jobDifficulty[0:i]) + dp(jobDifficulty[i:], d-1)) 
                memo[(n, d)] = mini
            return memo.get((n,d))
    
        return dp(jobDifficulty, d)
