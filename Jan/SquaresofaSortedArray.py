'''
# Two Pointers
977. Squares of a Sorted Array
給予一個有排序過的list, 
需回傳 non-decreasing 非遞減 的 order 的array, 
但不是隨便的array, 而是 the squares of each number 平方過後的number. 
'''


from operator import le


nums = [-4,-1,0,3,10]
list = []


'''
## two-pointers
Sort with O(n)
without deque
採用首置位跟末置位做比較，然後值大者入列

採用的方式是
         首             末
input = [-6, -4, 1, 2, 3, 5]

math.abs (-6) > 5 == True 

output = [0, 0, 0, 0, 0, 36]


             首           末
input = [-6, -4, 1, 2, 3, 5]

math.abs (-4) > 5 == False 

output = [0, 0, 0, 0, 25, 36]


'''

def sol(nums):
    # [-6, -4, 1, 2, 3, 5] 共6個數值

    # l = 0, r = 5
    l, r = 0, len(nums) -1
    print("預設r", r)
    # answer = [0, 0, 0, 0, 0, 0 ]
    answer = [0] * len(nums)
    # 當 0 < 5的
    while l <= r:
        # round 1:
        # left = nums[0] = 6
        # right = nums[5] = 5

        # round 2:
        # left = nums[1] = 4
        # right = nums[5] = 5

        # round 3:
        # left = nums[1] = 4
        # right = nums[4] = 3

        left, right = abs(nums[l]), abs(nums[r])
        print("開始的r:", r)
        # round 1:
        # 當 left (6) > right (5)
        # round 3:
        # 當 left (4) > right (3)
        if left > right:
            # round 1:
            # answer[5-0] = 36 || answer[5] = 36
            # answer[0, 0, 0, 0, 0, 36]
            # round 3:
            # answer[4 - 1] = answer[3] = 16
            # answer[0, 0, 0, 16, 25, 36]
            answer[r-l] = left * left
            print("r:", r)
            print("r-1:",r-1)
            # l = 0 + 1
            l += 1

        else:
            # round 2:
            # 當 left(4) < right(5)
            # answer[5-1] = answer[4] = 25
            # answer[0, 0, 0, 0, 25, 36]
            # 
            answer[r-l] = right * right
            # r = 5 - 1 = 4
            r -= 1

    return answer


# '''
# I tried:
# 直接用python的sort
# Time: 278 ms
# Space: 
# '''
# def sol():

#     i = 0
#     for num in nums:
#         i = num * num
#         list.append(i)
    
#     list.sort()
#     return list

sol(nums)