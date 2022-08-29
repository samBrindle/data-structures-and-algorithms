from data_structures.linked_list import LinkedList

class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024):
        # initialization here
        self.buckets = [None] * size
        self.size = size

    def set(self, key, value):
        # method body here
        i = self.hash(key)
        bucket = self.buckets[i]

        if not bucket:
            bucket = LinkedList()
            self.buckets[i] = bucket

        dic_ref = (key, value)
        bucket.insert(dic_ref)

    def get(self, key):
        hashcode = self.hash(key)
        bucket = self.buckets[hashcode]

        if bucket is None:
            return None
        drop = bucket.head

        while drop is not None:
            if drop.value[0] == key:
                return drop.value[1]
            drop = drop.next
        return None

    def contains(self, key):
        i = self.hash(key)
        bucket = self.buckets[i]

        if not bucket:
            return False
        return True

    def keys(self):
        all_keys = []

        for bucket in self.buckets:
            if bucket:
                curr = bucket.head
                while curr:
                    dic_ref = curr.value
                    all_keys.append(dic_ref[0])

        return all_keys

    def hash(self, key):
        ascii_sum = sum([ord(char) for char in key])
        i = (ascii_sum * 599) % self.size
        return i
