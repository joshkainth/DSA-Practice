import hashlib
class WordCounter:
    def __init__(self, words):
        self.words = words
        self.frequency = 1

    def __str__(self):
        return "{} [{}] times".format(self.words, self.frequency)

    # def split_review(self):
    #     split = []
    #     for word in self.words.split(" "):
    #         split.append(word)
    #
    #     return split

class HashTable:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = []

        for i in range(capacity):
            self.buckets.append(None)

    def hash_function(self, word):
        hash_code = int(hashlib.sha256(word.encode("utf-8")).hexdigest(), 16) % self.capacity
        return hash_code

    def put(self, words):

        for word in words.split():
            objects = WordCounter(word)
            index = self.hash_function(objects.words.lower())

            if self.buckets[index] is None:
                self.buckets[index] = objects
                self.size += 1
                print("^^ {} Inserted in HashTable | index {}".format(objects.words,index))
            else:
                self.buckets[index].frequency += 1
                print("## {} Frequency Updated to {} in HashTable | index {}".format(objects.words, objects.frequency, index))

    def iterate(self):
        count = 0
        print("~~~~~~~~~~~~~~")
        for word in self.buckets:
            if word is not None:
                print(word)
        print("~~~~~~~~~~~~~")

    def get(self, word):
        objects = WordCounter(word)
        index = self.hash_function(objects.words.lower())
        print(self.buckets[index])


review1 = "Really good institution teachers are very helpful and caring also environment of this " \
          "college is very attractive Proud to be a part of this college"
review2 = "Best institution Education level is high"
review3 = "What so ever I am today is due this technology Temple"
review4 = "Nice place a big also it provides you good education"
review5 = "Great institution with opportunities for those who want it"

capacity = len(review1.split()) + len(review2.split()) + len(review3.split()) + len(review4.split()) + len(review5.split())

hTable = HashTable(capacity)

hTable.put(review1)
hTable.put(review2)
hTable.put(review3)
hTable.put(review4)
hTable.put(review5)

hTable.iterate()

print("****************")
hTable.get("also")
print("****************")
print()


print("[Table Size] {} | [Total Words] {}".format(len(hTable.buckets), hTable.size))