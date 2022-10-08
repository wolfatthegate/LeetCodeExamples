# target = 2
#  i   lo        hi
# [-4, -1, 1, 2,  5]

# target - (i + lo + hi) = 2 - (-4 + -1 + 5) = 2  target > threesum => lo += 1 diff = 2
# target - (i + lo + hi) = 2 - (-4 + 1  + 5) = 0  target = threesum => hi -= 1 diff = 0
# target - (i + lo + hi) = 2 - (-4 + 1  + 2) = 3  target < threesum => hi -= 1 diff = 0

# target - (i + lo + hi) = 2 - (-1 + 1 + 5) = -3  target < threesum => hi -= 1 diff = 0
# target - (i + lo + hi) = 2 - (-1 + 1 + 2) = 0    target = threesum => hi -= 1 diff = 0

# target - (i + lo + hi) = 2 - (1 + 2 + 5) = -6  target < threesum => hi -= 1 diff = 0


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = inf 
        nums.sort()
        i = 0

        while i < len(nums): 
            lo = i + 1
            hi = len(nums) - 1
            while (lo < hi): 
                threesum = nums[i] + nums[lo] + nums[hi]
                if abs(target-threesum) < abs(diff): 
                    diff = target-threesum
                if threesum < target: 
                    lo += 1
                else: 
                    hi -= 1
            
            if diff == 0: 
                break
            i += 1

        return target - diff
            
