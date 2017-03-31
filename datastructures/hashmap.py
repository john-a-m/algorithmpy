_TOMBSTONE = type('_TOMBSTONE', (object,), {})

class HashMap:

    def __init__(self):
        self.size = 8
        self._buckets = [None] * self.size
        self.item_count = 0.
        
    def insert(self, key, value):

        num_of_buckets = len(self._buckets)
        if self.item_count / float(num_of_buckets) >= .75:
            print "resizing"
            self._resize(num_of_buckets * 4)

        index = hash_(key, self.size)

        #print self._buckets
        while self._buckets[index] is not None:
            index = rehash(index, self.size)
        print "inserted", key
        
        self._buckets[index] = (key, value)
        self.item_count += 1

    def get(self, key):
        
        index = hash_(key, self.size)
        item = self._buckets[index]

        if item is None:
            return None
        k, v = item
        if k == key:
            return v

        return self._find(key)
    
    def delete(self):
        self.item_count -= 1

    def _find(self, key):

        index = rehash(key, self.size)
        while True: #TODO no inf loop
            item = self._buckets[index]
            if item is None:
                return None
            k, v = item
            if k == key:
                return value
            index = rehash(index, self.size)
            
    def _resize(self, size):

        old = self._buckets
        self._buckets = [None] * size
        #self.item_count = size
        
        for bucket in (b for b in old if b and b != _TOMBSTONE):
            self.insert(*bucket)

def hash_(key, table_size):
    return key % table_size

def rehash(old_hash, table_size):
    return (old_hash + 1) % table_size

if __name__ == "__main__":

    hm =  HashMap()

    for n in range(100):
        hm.insert(n, n + 1)

    print 'getting'
    print hm.get(49)
