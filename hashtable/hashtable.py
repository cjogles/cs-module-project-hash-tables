class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"key = {self.key}, value = {self.value}, next = {self.next}"


class SinglyLinkedList:
    def __init__(self, first_node=None):
        self.head = first_node

    def __repr__(self):
        return f"head = {self.head}"


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.hash_table = [None] * self.capacity

    def __repr__(self):
        return f"hash_table = {self.hash_table}, size = {self.capacity}"

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        num_items = 0
        for i in self.hash_table:
            if i != None:
                num_items += 1
        print(num_items / self.capacity)
        return num_items / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """
        # Your code here
        # hash = offset_basis
        # for each octet_of_data to be hashed
        #     hash = hash * FNV_prime
        #     hash = hash xor octet_of_data
        # return hash
        # implemented
        fnv_offset_basis = 14695981039346656037
        fnv_prime = 1099511628211
        hashed_var = fnv_offset_basis
        string_bytes = key.encode()

        for b in sring_bytes:
            hashed_var = hashed_var * fnv_prime
            hashed_var = hashed_var ^ b

        return hashed_var

    def djb2(self, key):  # key will be a string
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        # one way to do it
        my_hash = 5381
        for x in key:
            my_hash = ((my_hash * 33) + ord(x))
        return my_hash

        # another way
        # my_hash = 5381
        # string_bytes = key.encode()

        # for b in string_bytes:
        #     my_hash = ((my_hash << 5) + my_hash) + b

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        # print("index = ", self.djb2(key) % self.capacity)
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        if self.get_load_factor() > 0.7:
            self.capacity = self.capacity * 2
            old_table = self.hash_table
            self.hash_table = [None] * self.capacity
            for i in old_table:
                curr = i.head
                while curr != None:
                    self.put(curr.key, curr.value)

        node_to_insert = self.hash_table[self.hash_index(key)]
        if node_to_insert is not None:
            old_head = node_to_insert.head
            node_to_insert.head = HashTableEntry(key, value)
            node_to_insert.head.next = old_head
        else:  # if None...
            self.hash_table[self.hash_index(key)] = SinglyLinkedList(
                HashTableEntry(key, value))

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        if self.hash_table[self.hash_index(key)] != None:
            curr = self.hash_table[self.hash_index(key)].head
            while curr != None:
                # print("###", curr)
                if curr.key == key:
                    curr.value = None
                    return
                curr = curr.next
            print("key not found!")

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
        if self.hash_table[self.hash_index(key)] == None:
            return None
        elif self.hash_table[self.hash_index(key)] != None:
            curr = self.hash_table[self.hash_index(key)].head
            while curr != None:
                if curr.key == key:
                    return curr.value
                curr = curr.next
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Your code here
        # double the array size, once the load factor gets close to 1 or above
        # then re-insert all of the items from the old hashtable into the new hashtable
        # using the hash function
        # lower load factor means fewer collisions, so a better perfomring hash table
        # good rule of thumb is resize when the load factor is greater then .7

        # make a new array, double size
        # iterate thorugh old array and old linked lists
        # insert into new array, same way we did in old array
        pass


# ----------------------------------
if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("key-0", "val-0")
    ht.put("key-1", "val-1")
    ht.put("key-2", "val-2")
    ht.put("key-3", "val-3")
    ht.put("key-4", "val-4")
    ht.put("key-5", "val-5")
    ht.put("key-6", "val-6")
    ht.put("key-7", "val-7")
    ht.put("key-8", "val-8")
    ht.put("key-9", "val-9")
    ht.get_load_factor()
    ht.delete("key-7")
    ht.delete("key-6")
    ht.delete("key-5")
    ht.delete("key-4")
    ht.delete("key-3")
    ht.delete("key-2")
    ht.delete("key-1")
    ht.delete("key-0")
    return_value = ht.get("key-0")
    print("$$$", return_value)
#     ht = HashTable(8)

#     ht.put("line_1", "'Twas brillig, and the slithy toves")
#     ht.put("line_2", "Did gyre and gimble in the wabe:")
#     ht.put("line_3", "All mimsy were the borogoves,")
#     ht.put("line_4", "And the mome raths outgrabe.")
#     ht.put("line_5", '"Beware the Jabberwock, my son!')
#     ht.put("line_6", "The jaws that bite, the claws that catch!")
#     ht.put("line_7", "Beware the Jubjub bird, and shun")
#     ht.put("line_8", 'The frumious Bandersnatch!"')
#     ht.put("line_9", "He took his vorpal sword in hand;")
#     ht.put("line_10", "Long time the manxome foe he sought--")
#     ht.put("line_11", "So rested he by the Tumtum tree")
#     ht.put("line_12", "And stood awhile in thought.")

#     print("")

#     # Test storing beyond capacity
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     # Test resizing
#     old_capacity = ht.get_num_slots()
#     ht.resize(ht.capacity * 2)
#     new_capacity = ht.get_num_slots()

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     print("")
# #-------------------------------------

# jackson = HashTable(10)
# jackson.put("howdy", 2)
# jackson.put("hi", 2)
# print(jackson)
# jackson.delete("hi")
# print(jackson)

# jackson.delete("potato")
# jackson.delete("apple")
# print(jackson)

# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None

#     def find(self, key):
#         current = self.head
#         while current is not None:
#             if current.key == key:
#                 return current # or the value if thats what you want
#             else:
#                 current = current.next
#         return current

#     def insert_at_head(self, key, value):
#         #check if the key  is already in the linked list
#         # find the node
#             current = self.head
#             while current is not None:
#                 # if the key is found, change the value
#                 if current.key == key:
#                     current.value = value
#                     # exit function immedietely
#                     return
#                 current = current.next
#         # if we reach the end of the list, its not there
#         # make a new node  and insert at head
#             new_node = HashTableEntry(key, value)
#             new_node.next = self.head
#             self.head = new_node

#     def insert_at_tail(self, key, value):
#         #check if the key  is already in the linked list
#         # find the node
#             current = self.head
#             while current is not None:
#                 # if the key is found, change the value
#                 if current.key == key:
#                     current.value = value
#                     # exit function immedietely
#                     return
#                 current = current.next
#         # if we reach the end of the list, its not there
#         # make a new node  and insert at tail
#             new_node = HashTableEntry(key, value)
#             new_node.next = self.head
#             self.head = new_node

#     def delete(self):
#         pass

# collision resolution iwth chaining, make a linked list work with hash table
# resizing - up. don't worry about down, that's a stretch goal.
