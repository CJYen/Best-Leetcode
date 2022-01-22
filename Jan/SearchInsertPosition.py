'''
# Binary Search
035 - Search Insert Position
!必需是O(log n)

找出target位於哪個index, 如果不在list中，你需要安插它到哪個index?

Input: 
nums = [1, 3, 5, 6],  target = 2

Output = 1
'''

'''
Time: 
Space: 
當找中間值小於 target 時，首置位換到 mid + 1 ，
相反的，如果中間值大於 target 時，末置位改到 mid - 1
找到不能再找為止，回傳 首
'''


nums = [2]
target = 1


def sol():
    left, right = 0, len(nums) - 1
    print("首置位 start", left)
    print("末置位 start", right)

    while left <= right:
        print("首置位現在", left)
        mid = (left + right) // 2
        print("中間值現在", mid)

        if nums[mid] < target: 
            left = mid + 1
            print("因為 target 大於目前的值，首置位往右移動", left)
        elif nums[mid] > target:
            right = mid - 1
            print("因為 target 小於目前的值，末置位往左移動", right)
        else: 
            print("最終值", mid)           
            return mid  

    print("更新後的首置位", left)
    return left


    '''
    為什麼是回傳left呢？
    
    當走到 M 跟 L 重疊時，因為此時的 L 要不就是將要加 1(然後再跳出)，要不就是已跳出

    [1, 3]
    2

    [1, 3]
    L    R
    M : 1//2 = 0
    M < 2

    [1, 3]
        L = 1
        R
        M > 2 

    跳出

    '''


sol()