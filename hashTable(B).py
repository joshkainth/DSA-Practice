class Student:
    def __init__(self, name, roll_no, age):
        self.name = name
        self.roll_no = roll_no
        self.age = age

    def __str__(self):
        return "{} \t {} \t {}".format(self.name,self.roll_no, self.age)

class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.table = []

        for i in range(capacity):
            objects = []
            # objects = cll.LinkedList()
            self.table.append(objects)

    def hash_function(self, key):
        hash_code = key % self.capacity
        return hash_code

    def put(self, student):
        # New Data is over-written on previous value which is present at that particular index
        key = student.roll_no + student.age
        index = self.hash_function(key)

        # if self.table[index] is None:
        self.size +=1

        self.table[index].append(student)
        print("Data Added {} at index {}".format(student,index))

    def search(self, student):
        key = student.roll_no + student.age
        index = self.hash_function(key)

        for key in self.table[index]:
            if key == student:
                print(student.name,"Found at index: ", index)
            else:
                print(student.name," not Found")

    def remove_key(self, student):
        key = student.roll_no + student.age
        index = self.hash_function(key)

        for key in self.table[index]:
            if key == student:
                self.table[index].remove(key)
                print(key," is removed from table")

    def iterate(self):
        for i in range(0, len(self.table)):
            if len(self.table[i]) != 0:
                print("--Index at {}---".format(i))
                for data in self.table[i]:
                    print(data)
                # print("----------------")

hTable = HashTable(5)
s1 = Student("John", 101, 22)
s2 = Student("Jack", 102, 20)
s3 = Student("Jenn", 102, 22)
s4 = Student("Adam", 104, 24)
s5 = Student("Jame", 105, 25)

hTable.put(s1)
hTable.put(s2)
hTable.put(s3)
hTable.put(s4)
hTable.put(s5)

hTable.iterate()
print("--Contains---")
hTable.search(s3)
print("-------------")

print("---Remove----")
hTable.remove_key(s4)
# hTable.remove_key()
print("-------------")
# print(hTable.table)
hTable.iterate()