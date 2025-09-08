class MinHeap:
    #now we creat the init func that python will activate automatic
    #this func will decide witch internal val will be to the new object
    def __init__(self):
        self.data = []
        self.size = 0

    def _parent(self, i):
        if i == 0:
            return None
        return (i - 1) // 2

    def _left(self, i):
        left = 2 * i + 1
        if left >= self.size:
            return None
        return left

    def _right(self, i):
        right = 2 * i + 2
        if right >= self.size:
            return None
        return right

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def peek(self):
        if self.is_empty():
            return None
        return self.data[0]

    def add(self, item):
        self.data.append(item)
        self.size += 1
        current_index = self.size -1
        while True:
            parent_index = self._parent(current_index)
            if parent_index is None:
                break
            elif self.data[parent_index] <= self.data[current_index]:
                break
            else:
                temp = self.data[parent_index]
                self.data[parent_index] = self.data[current_index]
                self.data[current_index] = temp
                current_index = parent_index

    def pop(self):
        if self.is_empty():
            return None
        temp = self.data[0]
        self.data[0] = self.data[self.size - 1]
        del self.data[self.size - 1]
        self.size -= 1
        if self.size == 0:
            return temp
        curr_index = 0
        while 1:
            left_index = self._left(curr_index)
            if left_index is None:
                break
            right_index = self._right(curr_index)
            if right_index is None:
                smaller_index = left_index
            elif self.data[left_index] > self.data[right_index]:
                smaller_index = right_index
            else:
                smaller_index = left_index
            if self.data[curr_index] <= self.data[smaller_index]:
                break
            self.data[curr_index], self.data[smaller_index] = self.data[smaller_index], self.data[curr_index]
            curr_index = smaller_index
        return temp

print("the file upload successfully")
h = MinHeap()
print(h.data)
print(h.size)
print(h.is_empty())
print(h.get_size())
h.add(1)
h.add(5)
h.add(2)
print(h.data)