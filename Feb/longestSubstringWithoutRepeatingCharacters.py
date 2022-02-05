'''
# 3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.
在string裡，找出它最大的substring, 需要連續並且非重覆字元。

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

'''
Think:

'''
s = "pwwkew"
def sol():
    charSet = set()
    l = 0
    res = 0
    '''
    if r already in charset, remove it, and shift l one step to the next(right).
    if r not in charset, add it into it, also compare the res value and save the maximum of it.
    '''
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res
    
sol()