# https://leetcode.com/problems/two-sum/

# # 方法一 Brute Force: 7827 ms 14.8 MB
# def twoSum(nums, target: int):
#     # 從第一個數開始 迴圈，如果list中有4個數值，就從一開始迴圈跑到最後一個
#     for i in range(len(nums)):
#         # 在每一次的迴圈中，扣除掉目前所在的數值，再做迴圈，到最後一個
#         for j in range(i + 1, len(nums)):
#             # 所以當目標值扣掉i所在的數值剛好等於j所在的數值，那就會得到i和j這兩個index了
#             if nums[j] == target - nums[i]:
#                 return [i, j]

# 方法二 One-pass Hash Table: 90 ms 15.2 MB
def twoSum(nums, target: int):
    # 先設一個seen，來依序裝進遇到過的數值
    seen = {}
    # 設一個遞迴的 for loop，從一開始的數值，這次我們要包含index, 和該index內的數值
    for i, value in enumerate(nums):
        # 把目標減去目前index內的數值，得到的數值存進變數 - remaining
        remaining = target - nums[i]
        print("1seen", seen)
        print("1remaining", remaining)
        # 如果檢查到變數 remaining 在 list 中
        if remaining in seen:
            r = [i, seen[remaining]]
            print("2seen", seen)
            print("2remaining", remaining)
            return r
        # 把遇到的值存到seen
        seen[value] = i
        print("3seen", seen)
        print("3remaining", remaining)
        
    

result1 = twoSum([2,7,11,15], 9)
# result2 = twoSum([3,2,4], 6)
# result3 = twoSum([3,3], 6)
print(result1)
# print(result2)
# print(result3)
# print("hello world")


