from collections import deque
class Node:
    def __init__(self,val = None,next = None):
        self.val = val
        self.next = next

class ll:
    def __init__(self):
        self.head = None

    def add_last(self, val):
        if not self.head:
            self.head = Node(val)
        else:
            head = self.head
            t = Node(val)
            while head.next:
                head = head.next
            head.next = t
    def display(self):
        head = self.head
        while head:
            print(head.val, ' --> ', end='')
            head = head.next
        print()

    def add_rec(self,val,pos,head,prev=None):
        if pos == 0:
            t = Node(val,head)
            if prev:
                prev.next = t
            else:
                self.head = t
            return
        self.add_rec(val,pos-1,head.next,head)

    def mid(self, head):
        fp = sp = prev = head
        while fp and fp.next:
            prev = sp
            sp = sp.next
            fp = fp.next.next
        prev.next = None
        return sp

    def merge(self, f, s):
        res = Node()
        ans = res
        while f and s:
            if f.val < s.val:
                ans.next = f
                f = f.next
                ans = ans.next
            else:
                ans.next = s
                s = s.next
                ans = ans.next
        if f:
            ans.next = f
        if s:
            ans.next = s
        return res.next

    def mergesort(self, head):
        if not head or not head.next:
            return head

        mid = self.mid(head)
        left = self.mergesort(head)
        right = self.mergesort(mid)

        return self.merge(left, right)

    def reverse(self):
        head = self.head
        prev = None
        while head:
            t = head.next
            head.next = prev
            prev = head
            head = t
        self.head = prev

    def reverse_rec(self,head):
        if not head.next:
            self.head = head
            return head

        node = self.reverse_rec(head.next)

        node.next = head
        head.next = None
        return head




    res = deque()
    max = 0
    def rec(self, head):
        if not head.next:
            self.res.appendleft(0)
            self.max = head.val
            return

        self.rec(head.next)
        if self.max < head.val:
            self.res.appendleft(0)
            self.max = head.val
        else:
            self.res.appendleft(self.max)

    def nextLargerNodes(self, head):
        self.rec(head)
        return self.res

if __name__ == '__main__':
    list = ll()
    arr = [2,7,4,3,5]
    arr= [2,1,5]
    for i in arr:
        list.add_last(i)
    list.display()
    '''    
    list.add_rec(4,3,list.head)
    list.add_last(0)
    list.add_last(5  )
    list.display()
    list.head = list.mergesort(list.head)
    list.display()
    list.reverse()
    list.display()
    list.reverse_rec(list.head)
    list.display()
    '''
    arr = list.nextLargerNodes(list.head)
    print(list(arr))