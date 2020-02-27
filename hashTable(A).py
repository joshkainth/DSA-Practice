# Open Hashing
class HashTable:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.table = []

        for i in range(capacity):
            objects = []
            self.table.append(objects)

    def hash_function(self, key):
        hash_code = key % self.capacity
        return hash_code

    def put(self, data):
        # New Data is over-written on previous value which is present at that particular index
        index = self.hash_function(data)

        # if self.table[index] is None:
        self.size +=1

        self.table[index].append(data)
        print("Data Added {} at index {}".format(data,index))

    def search(self, data):
        index = self.hash_function(data)

        for key in self.table[index]:
            if key == data:
                return index
                # print(data," Found at index: ", index)
            else:
                return self.search(key)
                # print(data," not Found")

    def remove_key(self, data):
        index = self.hash_function(data)

        for key in self.table[index]:
            if key == data:
                self.table[index].remove(key)
                print(key," is removed from table")

    def iterate(self):
        for i in range(0, len(self.table)):
            if len(self.table[i]) != 0:
                print("--Index at {}---".format(i))
                for data in self.table[i]:
                    print(data)
                # print("----------------")

hTable = HashTable(15)
hTable.put(60)
hTable.put(14)
hTable.put(48)
hTable.put(75)
hTable.put(35)
hTable.put(110)
hTable.put(12)
hTable.put(56)

print(hTable.table)
print("Total Element Added: ",hTable.size)

print("--Contains---")
print(hTable.search(110))
print(hTable.search(56))
# hTable.search(110)
# hTable.search(56)
print("-------------")

print("---Remove----")
hTable.remove_key(48)
hTable.remove_key(110)
print("-------------")

print(hTable.table)
print(len(hTable.table))
# hTable.iterate()