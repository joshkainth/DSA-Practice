class ProductDetails:
    def __init__(self, title, rating, deal, price, delivery_date):
        self.title = title
        self.rating = rating
        self.deal = deal
        self.price = price
        self.delivery_date = delivery_date

    def show_product_info(self):
        print("{}\t |\t {} |\t {} |\t {} | {}".format(self.title, self.rating, self.deal, self.price,
                                                      self.delivery_date))

class Node:
    def __init__(self, data, target_node):
        self.data = data
        self.target_node = target_node

    def show_node(self):
        # print("{} | ".format(self.data), end=" ")
        self.data.show_product_info()

class LinkedList:
    head = None
    tail = None
    __list_size = 0

    def add_node(self, data):

        node = Node(data, None)
        # print("[Appended Node]address ", node)

        if LinkedList.head is None:
            LinkedList.head = node
            LinkedList.tail = node
            print("[Appended Node]address: {} | [LinkedList.head]: {} | [LinkedList.head.target_node]: "
                  "{} | [LinkedList.tail]: {}".format(node, LinkedList.head, LinkedList.head.target_node, LinkedList.tail))
        else:
            LinkedList.tail.target_node = node
            LinkedList.tail = node
            print("[Appended Node]address: {} | [LinkedList.head]: {} | [LinkedList.head.target_node]: "
                  "{} | [LinkedList.tail]: {} | [LinkedList.tail.target_node]: {}".format(node, LinkedList.head, LinkedList.head.target_node,
                                                      LinkedList.tail, LinkedList.tail.target_node))

    def add_node_at_beginning(self,data):

        node = Node(data, None)
        # print("[Appended Node]address ", node)

        temp = LinkedList.head
        LinkedList.head = node
        node.target_node = temp

        print("[Appended Node]address: {} | [LinkedList.head]: {} | [LinkedList.head.target_node]: "
              "{}".format(node, LinkedList.head, LinkedList.head.target_node))

    def show_details(self, node):

        if node.target_node is None:
            node.show_node()
            return

        node.show_node()
        self.show_details(node.target_node)

    def selection_sort(self):
        current = LinkedList.head
        next_node = LinkedList.head.target_node

        while current.target_node is not None:
            if current.data.price > next_node.data.price:
                LinkedList.head = next_node

                current.target_node = next_node.target_node
                print(current.show_node())
                next_node.target_node = current

                print(next_node.show_node())

            current = next_node
            next_node = next_node.target_node


pref1 = ProductDetails("IPhone 11", 4.5, "30% off", 75260, "January 24")
pref2 = ProductDetails("IPhone Xs", 4.3, "25% off", 65410, "January 25")
pref3 = ProductDetails("Samsung A10", 3.5, "20% off", 15620, "January 15")
pref4 = ProductDetails("Samsung A8", 3.8, "10% off", 14650, "January 6")
pref5 = ProductDetails("Samsung A6", 3.8, "10% off", 13550, "February 10")

lRef = LinkedList()

lRef.add_node(pref1)
lRef.add_node(pref2)
lRef.add_node(pref5)
# lRef.add_node_at_beginning(pref3)
# lRef.add_node_at_beginning(pref4)

lRef.show_details(LinkedList.head)
print("Before Sorting")

lRef.selection_sort()
print("List after sorting")
lRef.show_details(LinkedList.head)


        # while current.target_node is not None:
        #     while next_node.target_node is not None:
        #         if current.data.price > next_node.data.price:
        #             temp = current.data.price
        #             current.data.price = next_node.data.price
        #             next_node.data.price = temp