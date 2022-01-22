#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
# @lc code=end
        x = 0
        for i in nums:
            # print(x)
            if i == target:
                nums[x] = i
                print(x)
                return x
            else:
                x += 1
