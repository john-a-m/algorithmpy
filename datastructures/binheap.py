class BinHeap:

    def __init__(self):
        
        self._heap = [0]
        self._heap_size = 0

    def _swap_up(self, index):

        while index // 2 > 0:
            
            parent = self._heap[index // 2]
            child = self._heap[index]
            
            if child < parent:
                self._heap[index], self._heap[index // 2] = parent, child

            index = index // 2
            
    def _swap_down(self, index):

        while (index * 2) <= self._heap_size:
            
            child_index = self._min_child(index)
            child = self._heap[child_index]
            parent = self._heap[index]
            
            if parent > child:
                self._heap[child_index], self._heap[index] = parent, child

            index = min_child_index

    def _min_child(self, index):

        #indexes of the left and right children
        left_child = index * 2
        right_child = index * 2 + 1
        
        if right_child > self._heap_size:
            return left_child
        else:
            if self._heap[left_child] < self._heap[right_child]:
                return left_child
            else:
                return right_child

    def insert(self, value):
        
        self._heap.append(value)
        self._heap_size += 1
        self._swap_up(self._heap_size)

    def del_min(self):
        
        root = self._heap[1]
        self._heap[1] = self._heap[self._heap_size]
        del self._heap[self._heap_size]
        self._heap_size -= 1
        self._swap_down(1)
        return root

if __name__ == "__main__":

    heap = BinHeap()
    heap.insert(100)
    heap.insert(1)

    print heap.del_min()
    print heap._heap
    #print heap.del_min()
