# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        binNum = [head.val]
        while(head.next != None):
            binNum.append(head.next.val)
            head = head.next
        
        total = 0
        BASE = 2
        exp = 0
        for i in range(len(binNum) - 1, -1, -1):
            if binNum[i] != 0:
                total += pow(BASE, exp)
            exp += 1
        
        return total

        

def main():
    sol = Solution()
    test = ListNode(1, ListNode(0, ListNode(1, None)))
    x = sol.getDecimalValue(test)
    print(x)



if __name__ == '__main__':
    main()