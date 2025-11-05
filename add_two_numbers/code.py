# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        self.l1 = l1
        self.l2 = l2

        result_list = []
        carry = 0

        while True:
            try:
                try:
                    l1_num = self.l1.val

                except Exception as e:
                    if carry == 1: l1_num = 0
                    else: break

                try:
                    l2_num = self.l2.val

                except Exception as e:
                    l2_num = 0

                result = l1_num + l2_num + carry

                if result >= 10:
                    stored_result = result - 10
                    result_list.append(stored_result)
                    carry = 1
                
                else:
                    result_list.append(result)
                    carry = 0
                
                self.l1 = self.l1.next

                try:
                    self.l2 = self.l2.next

                except Exception as e:
                    pass

            except AttributeError:
                break
        
        node_list = []
        for num in result_list:
            node_list.append(
                ListNode(val=num, next=None)
                )

        list_length = len(node_list)
        if list_length > 1:
            for index in range(list_length - 1):
                node_list[index].next = node_list[index + 1]


        return node_list[0]