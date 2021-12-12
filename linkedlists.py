class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beg(self, data):
        node = Node(data, self.head)
        self.head = node

    def lprint(self):
        if self.head is None:
            print("list is empty")
            return
        itr = self.head
        lv = ""
        while itr:
            lv += str(itr.data) + "-->"
            itr = itr.next
        print(lv)

    def insert_end(self, data):
        node = Node(data)
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at(self,idx,data):
        if idx == 0:
            self.insert_beg(data)
            return
        if idx == self.get_length()-1:
            self.insert_end(data)
            return
        count = 0
        node = Node(data)
        itr = self.head
        while itr:
            if count == idx-1:
                node.next, itr.next = itr.next.next, node
            count += 1
            itr = itr.next
        return

    def insert_after(self,idx,data):
        itr = self.head
        while itr:
            if itr.data == idx:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_at(self, idx):
        length = self.get_length()
        if idx < 0 or idx >= length:
            raise Exception("invalid index")
        if idx == 0:
            self.head = self.head.next
            return
        itr = self.head
        count = 0
        while itr:
            if count == idx-1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def remove_value(self,data):
        itr = self.head
        while itr:
            if itr.data == data:
                pitr.next = itr.next
                break
            pitr = itr
            itr = itr.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_beg(5)
    ll.insert_beg(8)
    ll.insert_beg(3)
    ll.insert_end(10)
    ll.insert_beg(7)
    ll.lprint()
    ll.remove_at(0)
    ll.lprint()
    ll.remove_at(2)
    ll.lprint()
    ll.insert_at(0, 20)
    ll.insert_at(2, 30)
    ll.lprint()
    ll.insert_after(10,100)
    ll.lprint()
    ll.insert_after(3,300)
    ll.lprint()
    ll.remove_value(10)
    ll.lprint()