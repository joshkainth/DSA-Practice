class HashTable:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.table = []

        for i in range(capacity):
            self.table.append(None)

    def hash_function(self, key):
        hash_code = key % self.capacity
        return hash_code

    def put(self, data):
        # New Data is over-written on previous value which is present at that particular index
        index = self.hash_function(data)

        if self.table[index] is None:
            self.size +=1

        self.table[index] = data
        print("Data Added {} at index {}".format(data,index))

    '''def put(self, data):
        # Data will not added in table when if data is already present at that particular index
        index = self.hash_function(data)

        if self.table[index] is None:
            self.size += 1
            self.table[index] = data
            print("Data Added {} at index {}".format(data, index))
        else:
            print("{} will not be added. Please try another value".format(data))'''

    def search(self, data):
        index = self.hash_function(data)

        if self.table[index] == data:
            return index
        else:
            return -1

    def iterate(self):
        for data in self.table:
            if data is not None:
                print(data)

    def remove(self, data):
        index = self.hash_function(data)
        if self.table[index] == data:
            self.table[index] = None
            print(data, "is removed from table :)")
        else:
            print("Sorry!!, ", data, " not found in table :(")

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
print(hTable.search(75))
print(hTable.search(60))
print("-------------")

print("---Remove----")
hTable.remove(75)
hTable.remove(60)
print("-------------")

hTable.iterate()