'''
# 876. Middle of the Linked List
傳回中間值的linked list
Input: head = [1,2,3,4,5]
Output: [3,4,5]

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
'''


from imports import ListNode


head = [1,2,3,4,5,6]
head = [1,2,3,4,5]



def middleNode(head: ListNode) -> ListNode:
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]



middleNode(head)