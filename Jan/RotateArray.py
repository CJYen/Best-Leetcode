'''
# 189. Rotate Array
給的array, 將它按照k次回轉

例:
nums = [1, 2, 3, 4, 5, 6, 7], k = 3
後續步驟:
迴轉第1次: [7,1,2,3,4,5,6]
迴轉第2次: [6,7,1,2,3,4,5]
迴轉第3次: [5,6,7,1,2,3,4]

最終得到 [5,6,7,1,2,3,4]

並且，至少有三種方法解決這個問題，
以及能不能以 space = O(1) 解決？
'''

nums = [-1,-100,3,99]
k = 2
# output 預期 = [3,99,-1,-100]

def sol(nums, k):
    # print("方法2")    
    n = len(nums)
    k = k % n
    # nums[4-2:] + nums[:4-2]
    # nums[2:] + nums[:2]
    # nums[3, 99] + nums[-1, -100]
    nums[:] = nums[n-k:] + nums[:n-k]

    # print("方法1")
    # # 先取得 k 被 list 數量除過後的餘數 k = 2 % 4 = 2
    # k = k % len(nums)
    # # l = 0, r = 4 -1 = 3
    # l, r = 0, len(nums) -1

    # # 先整個 reverse
    # # 1 : 當 0 < 3 時
    # # 2 : => 1 < 2
    # while l < r:
    #     # 1 : 將nums的頭尾對掉 nums[99, -100, 3, -1]
    #     # 2 : nums[99, 3, -100, -1]
    #     nums[l], nums[r] = nums[r], nums[l]
    #     # 1 : l = 0 + 1, r = 3 - 1 
    #     # 2 : l = 1 +1, r = 2 -1
    #     l, r = l + 1, r -1
    
    # # 為了只按照 k 來切分做最後的 reverse，先找出應該要reverse的部分，以k-1去抓第一部分
    # l, r = 0, k -1
    # while l < r:
    #     nums[l], nums[r] = nums[r], nums[l]
    #     l, r = l + 1, r -1

    
    # # 後面剩下的部分再做最後的 reverse
    # l, r = k, len(nums) - 1
    # while l < r:
    #     nums[l], nums[r] = nums[r], nums[l]
    #     l, r = l + 1, r -1
    

        
    


sol(nums, k)