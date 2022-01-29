'''
# 283. Move Zeroes
在一組array當中，除了將所有的 0 移到排序的最後，其餘的排序不變。

Example
Input: 
nums = [0,1,0,3,12]
Output: 
[1,3,12,0,0]


'''
nums = [0,1,0,3,12]

def sol():
    j = 0
    for i in range(len(nums)):
        print("i",i)
        if nums[i] != 0:
            print("1st",nums)
            nums[j], nums[i] = nums[i], nums[j]
            print("2st",nums)
            i += 1
    print("final:", nums)

    # # 1st, try
    # list = [0] * len(nums)
    # l, r = 0, len(nums) - 1

    # for i in nums:
    #     # print("i",i)
    #     if i != 0:
    #         list[l] = i
    #         l += 1          
    #     else:
    #         list[r] = i
    #         r -= 1
    # nums[:] = list[:]
    # print(nums)

sol()