'''
# 1672. Richest Customer Wealth
在一組grid中，要找出每個帳戶總額最高者

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.

'''

accounts = [[1,5],[7,3],[3,5]]


'''
Space complexity: O(1)
Time complexity: O(M⋅N)
先用sum 把array裡的值加總暫存起來，再一對一的進行比較，留下最值最大者。
'''

def sol():
    max_wealth = 0
    for account in accounts:
        curr_wealth = sum(account)
        max_wealth = max(max_wealth, curr_wealth)
    return (max_wealth)
sol()