# 704. Binary Search
# from traceback import print_tb

''' 
預想:
假設中間值剛好是我們要的target, 那我們就回傳該index
假設target比中間值還小，就往左找
相反的，就往右找

left    m  -->   right
[-1, 0, 3, 5, 9, 12] target 9

'''

def sol():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9

    # 先設定首置位和末置位
    left, right = 0, len(nums) - 1
    # 當末置位大於首置位的時候，取中間值
    while left <= right:
        pivot = left + (right - left) // 2
        # 當中間值等於target就回傳index
        if nums[pivot] == target:
            print("Found it!", pivot)
            return pivot
        # 如target大於中間值就繼續往右邊找
        if target > nums[pivot]:
            print("smaller than target, search the right")
            left = pivot + 1
        # 相反的，就找左邊
        else:
            print("larger than target, search the left")
            right = pivot - 1
    print("cannot found, return -1")
    return -1

    # I tried
    # x = 0
    # for i in nums:
    #     if i < target:
    #         x += 1
    #     elif i == target:
    #         nums[x] = i
    #         print("x",x)
    #         return x
    #     else:
    #         print(-1)

sol()