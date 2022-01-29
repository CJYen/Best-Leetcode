'''
# 557 revers words in a sting III
給予一字串s, 將它裡面的characters順序反轉，並同時維持它原本的whitespace 和原本句子的排列。

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Input: s = "God Ding"
Output: "doG gniD"

'''

s = "God Ding"
s = "Let's take LeetCode contest"

'''
Time : O(n)
Space : O(n)

先將string 切分成 list, 
並將之反轉後join起來，
最後整個再次反轉。

# s.split()[::-1] 把它切分成list
['contest', 'LeetCode', 'take', "Let's"]

# ' '.join(s.split()[::-1]) 將之join起來
contest LeetCode take Let's

# ' '.join(s.split()[::-1])[::-1] 最後整個再反轉
s'teL ekat edoCteeL tsetnoc
'''

def sol():
    print(s.split()[::-1])
    print(' '.join(s.split()[::-1]))
    print(' '.join(s.split()[::-1])[::-1])
    return ' '.join(s.split()[::-1])[::-1]
    
sol()