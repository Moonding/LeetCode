# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        list3_head = None
        list3 = None
        
        while list1 or list2:       
            if list1 is None or list2 and list1.val > list2.val:
                if list3_head is None:
                    list3_head = ListNode(list2.val)
                    list2 = list2.next
                    list3 = list3_head
                    continue
                list3.next = ListNode(list2.val)
                list3 = list3.next
                list2 = list2.next
                
            else:
                if list3_head is None:
                    list3_head = ListNode(list1.val)
                    list1 = list1.next
                    list3 = list3_head
                    continue
                list3.next = ListNode(list1.val)
                list3 = list3.next
                list1 = list1.next
            
        return list3_head