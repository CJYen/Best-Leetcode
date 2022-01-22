'''
# Binary Search
278. First Bad Version
在n裡面，如果bad的值之後，都會是false
想像你是產品經理，當你知道某個版本的build是錯的，
在它之後的build都會是錯的，試想你可以怎麼找出它們

Input:
n = 5, bad = 4
output:
4

在4以後的都是錯的
*isBadVersion() api 已經預先處理好了
'''

n = 5
bad = 4

# def isBadVersion(i):
#     if i == bad:
#         return True
#     else: 
#         return False


'''
Time: O(n)
Space: O(1)
從頭一個一個找，直到找到為止

'''

def sol():

    # 在這個range裡，當呼叫的isBadVersion api回傳True時，回傳給我
    for i in range(n):
        if (isBadVersion(i)==True):
            return i
    # 否則就直接回傳n
    return n


'''
Time: O(log n)
Space: O(1)

如果在遇到壞版本的情況下，就再繼續往更早的版本查下去，
直到查到不能再查為止
'''
def sol2():

    left = 1
    right = n
        
    # 當 n 大於 1 時，如果遇到的壞版本的情況下，將 mid 設成末置位
    while left < right:
        mid = int(left + ( right - left) / 2)
        print("mid", mid)

        if isBadVersion(mid) == True:
            right = mid
            print("Bad version! ", int(right))
        # 相反的，如果遇到好版本，將 mid 設成首置位去找
        else:
            left = mid + 1
            print("Now it's good version ",int(left))

    # 查到不能再查的時候，就回傳 left
    print("Found ",int(left))
    return int(left)


sol2()
