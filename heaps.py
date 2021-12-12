"""
import heapq
arr = [10,9,5,3,2,1]
heapq.heapify(arr)
print(arr)
heapq.heappush(arr,15)
print(arr)
"""
class heap:
    def __init__(self,size):
        self.size = size
        self.arr = [None] * (size+1)
        self.arr[0] = size
        self.len = 0
        self.last = 1

    def add(self,val):
        if self.last == self.size -1:
            self.arr.extend([None]*self.size)
        self.arr[self.last] = val
        if self.last > 1:
            self.add_check(self.last)
        self.len += 1
        self.last += 1

    def add_check(self,idx):
        if idx == 1: return
        val = self.arr[idx]
        if val > self.arr[idx//2]:
            self.arr[idx], self.arr[idx//2] = self.arr[idx//2],self.arr[idx]
            self.add_check(idx//2)

    def display(self):
        for i in self.arr[1:]:
            if not i: break
            print(i,end=' -> ')
        print()

    def pop(self):
        if not self.arr[1]: return None
        val = self.arr[1]
        self.arr[1] = self.arr[self.last-1]
        self.arr[self.last-1] = None
        self.last -= 1
        self.len -= 1
        self.pop_check()
        return val

    def pop_check(self,top = None):
        if not top:
            top = 1
        if top >= self.len or not self.arr[top*2]:
            return
        if top*2 > self.last or (top*2)+1 > self.last:
            return
        val = self.arr[top]
        if not self.arr[(top*2)+1] or self.arr[top*2] > self.arr[(top*2)+1]:
            if val < self.arr[top*2]:
                self.arr[top], self.arr[top * 2] = self.arr[top * 2], self.arr[top]
                self.pop_check(top * 2)
        else:
            if val < self.arr[(top*2)+1]:
                self.arr[top], self.arr[(top*2)+1] = self.arr[(top*2)+1], self.arr[top]
                self.pop_check((top*2)+1)

    def heapsort(self):
        l = self.len
        for i in range(l):
            val = self.pop()
            self.arr[self.last] = val
            print(val)
            #print(self.last)
if __name__ == '__main__':
    arr = [5,3,17,10,84,19,6,22,9]
    h = heap(len(arr)+1)
    for i in arr:
        h.add(i)
    h.display()
    h.heapsort()
    h.display()