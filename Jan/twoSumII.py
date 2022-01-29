'''
# 167. Two Sum II - Input Array Is Sorted
在已經sort的list裡，找出相加後為target的值，答案只有一組，不能重覆。
例如:
numbers = [0,0,3,4]
target = 0

output: [1, 2]
因為第一個0 加上第二個0 等於0
'''


# case:
numbers = [3,24,50,79,88,150,345]
target = 200

# case:
numbers = [0,0,3,4]
target = 0

# case:
numbers = [2,7,11,15]
target = 9

'''
two pointer的解法 
----------------
左置位、右置位先定義l, r
直找到左、右置位相加等於target前不會停止，
如果相加後小於target, 表示l 要向前一步，
相反的，表示r 要後退一步。
'''
def sol():
    l, r = 0, len(numbers) - 1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return[l+1, r+1]
        elif s < target:
            l += 1
        else:
            r -= 1

sol()