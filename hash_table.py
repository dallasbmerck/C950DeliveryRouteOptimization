# Class declaration for a hash table that utilizes chaining.
class HashMap:

    # All new buckets are assigned to an empty list.
    # O(1)
    def __init__(self, start_capacity=10):
        self.map = []
        for i in range(start_capacity):
            self.map.append([])

    # Finds the bucket list to insert the item into.
    # O(1)
    def find_bucket_list(self, key):
        return int(key) % len(self.map)

    # Puts a new item into the chaining hash table and gives it a bucket to reside in.
    # O(n)
    def insert(self, key, item):
        key_hash = self.find_bucket_list(key)
        key_value = [key, item]

        if self.map[key_hash] == None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True
            self.map[key_hash].append(key_value)
            return True

    # Allows for the updating of items that already exist in the bucket list.
    # Prints an error message if the item is not updated.
    # O(n)
    def update(self, key, value):
        key_hash = self.find_bucket_list(key)
        if self.map[key_hash] != None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])
                    return True
        else:
            print('Error updating value associated with key: ' + key)

    # Searches for items if they have a matching in the chaining hash table.
    # If the item is not found it returns None and returns the item if found.
    # O(n)
    def get_value(self, key):
        key_hash = self.find_bucket_list(key)
        if self.map[key_hash] != None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Finds the associated key of and removes its value.
    # O(n)
    def delete(self, key):
        key_hash = self.find_bucket_list(key)
        if self.map[key_hash] == None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False


class EnterIntoHashMap:
    def __init__(self, key, item):
        self.key = key
        self.item = item
