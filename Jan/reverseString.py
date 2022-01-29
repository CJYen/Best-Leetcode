'''
# 344 reverse string
透過一個function，來將input的string 內所有的characters反轉。
需使用O(1)的額外memory, 來直接改變這個input array。

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

'''

# s = ["H","a","n","n","a","h"]
s = ["h","e","l","l","o"]

'''
two pointer:
左置位、右置位先定義l, r
在左置位比右置位小的情況下，
先將左置位存到tmp, 
再將右置位存入左置位，
左置位再向右一格
再將tmp存入右置位，
右置位再向左一格

Round 1
  l               r
["h","e","l","l","o"]

# tmp = s[l]
tmp = "h"

# s[l] = s[r]
  l               r
["o","e","l","l","o"]

# l +=1
      l           r
["o","e","l","l","o"]

# s[r] = tmp
      l           r
["o","e","l","l","h"]

# r -= 1
      l       r
["o","e","l","l","h"]
'''

def sol():
    l, r = 0, len(s) - 1
    while l < r:
        tmp = s[l]
        s[l] = s[r]
        l +=1
        s[r] = tmp
        r -= 1
    print(s)

'''
One line two pointer
Time complexity is O(n) and additional space is O(1).

'''
def sol():
    for i in range(len(s)//2):
        s[i], s[-i-1] = s[-i-1], s[i]
    print(s)

sol()