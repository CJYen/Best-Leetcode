'''
# 19. Remove Nth Node From End of List


'''


class ListNode:
    def __init__(self, data): 
        self.data = data
        # store the reference (next item)
        self.next = None
        return
  

class SingleLinkedList:
    # 初始化的時候，self.head = None, self.tail = None
    def __init__(self): 
        self.head = None
        self.tail = None
        return

    def add_list_item(self, item):
        # 加入一個值(例如19)這個item, 首先會轉換成ListNode
        if not isinstance(item, ListNode):
            item = ListNode(item)
        
        if self.head is None:
            self.head = item
        else:
            # 如果進入沒有判定的條件, 會把tail設定為新增的元素
            # ListNode(19), head和tail為ListNode(19), 則data為19，next為None
            self.tail.next = item
        self.tail = item
        return

    def output_list(self):

        current_node = self.head
        results = []
        
        while current_node is not None:
            results.append(current_node.data)

            # jump to the linked node
            current_node = current_node.next 
        print(results)
        return
    
list1 = SingleLinkedList()
list1.add_list_item(18)
list1.add_list_item('12')

'''
所以一開始加了18的item, 再加入12這個item, 首先加入時都會先轉為ListNode
if not isinstance(item, ListNode):
    item = ListNode(item)
然後因為head是18了，所以會進入else
    self.tail.next = item
那結果會長這樣
ListNode目前head為18，next為ListNode("12")
再把tail設定為新增元素
self.tail = item
[ListNode(18), ListNode("12")]，head為ListNode(18)，tail為ListNode("12")
ListNode(18)目前data為18，next為ListNode("12")，ListNode("12")目前data為"12"，next為None
'''

list1.output_list()

# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         fast = slow = head
#         for i in range(n):
#             fast = fast.next
#         if not fast: return head.next
#         while fast.next:
#             fast, slow = fast.next, slow.next
#         slow.next = slow.next.next
#         return head