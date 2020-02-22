class Products:
    def __init__(self, pid, title, rating, deal, price, delivery_date):
        self.pid = pid
        self.title = title
        self.rating = rating
        self.deal = deal
        self.price = price
        self.delivery_date = delivery_date

    def show_product_info(self):
        print("{}\t | {}\t |\t {} |\t {} |\t {} | {}".format(self.pid, self.title, self.rating, self.deal, self.price,
                                                      self.delivery_date))

class LinkedList:

    __size = 0
    total_amount = 0

    def __init__(self):
        self.head = None
        self.current = None

    def push_operation(self, product_object):

        LinkedList.__size += 1
        LinkedList.total_amount += product_object.price

        product_object.next = None
        product_object.previous = None
        print(">> Product Details of {}: {}".format(product_object.title, product_object.__dict__))
        print(">> Product hash address of {} : {}\n".format(product_object.title, product_object))

        if self.head is None:
            self.head = product_object
            self.current = product_object
            # print(">> NEXT {} PREVIOUS {}".format(product_object.next, product_object.previous))
            # print()
        else:
            self.current.next = product_object
            product_object.previous = self.current

            self.head.previous = product_object
            self.current = product_object
            self.current.next = self.head
            # print(">> NEXT {} PREVIOUS {}".format(product_object.next, product_object.previous))
            # print()

    def append_at_beginning(self, product_object):

        LinkedList.__size += 1
        LinkedList.total_amount += product_object.price

        product_object.next = None
        product_object.previous = None
        print(">> Product Details of {}: {}".format(product_object.title, product_object.__dict__))
        print(">> Product hash address of {} : {}\n".format(product_object.title, product_object))

        temp = self.head
        self.head = product_object

        self.head.next = temp
        self.head.previous = self.current
        self.current.next = self.head

        temp.previous = product_object

        # print(">> NEXT {} PREVIOUS {}".format(product_object.next, product_object.previous))

    def insertion_sort(self):

        temp = self.head

        while temp.next is not self.head:
            pass

        if temp.price > temp.next.price:
            value = self.head

    def remove_product(self, product_name):

        LinkedList.__size -= 1

        temp = self.head            # temp -> current,  target -> previous
        target = None

        while temp.next is not self.head:
            if temp.title == product_name:

                address1 = temp.next
                target.next = address1
                temp.next.previous = target

                LinkedList.total_amount -= temp.price

                del temp
                break

            target = temp
            temp = temp.next

    def remove_head(self):
        LinkedList.__size -= 1

        temp = self.head
        self.head = temp.next
        self.head.previous = self.current
        self.current.next = self.head

        LinkedList.total_amount -= temp.price

        del temp

    def pop_operation(self):
        LinkedList.__size -= 1

        temp = self.current
        self.current = self.current.previous
        self.current.next = self.head
        self.head.previous = self.current

        LinkedList.total_amount -= self.current.price

        del temp

    def move_forward(self):
        temp = self.head
        while temp.next is not self.head:
            temp.show_product_info()
            temp = temp.next
        temp.show_product_info()

    def move_backward(self):
        temp = self.current
        while temp.previous is not self.current:
            temp.show_product_info()
            temp = temp.previous
        temp.show_product_info()

    def total_products(self):
        return LinkedList.__size

lRef = LinkedList()
lRef.append_product(Products(101, "IPhone 11", 4.5, "30% off", 75260, "January 24"))
lRef.append_product(Products(201, "IPhone Xs", 4.3, "25% off", 65410, "January 25"))
lRef.append_product(Products(301, "Samsung A10", 3.5, "20% off", 15620, "January 15"))

lRef.append_product(Products(401, "Samsung A8", 4.2, "15% off", 13260, "February 15"))
lRef.append_product(Products(501, "Samsung A6", 3.8, "10% off", 13550, "February 10"))

print("\n>> Linked List: ", lRef.__dict__)
print("\nForward Move:")
lRef.move_forward()
#
print("\nBackward Move: ")
lRef.move_backward()

print("\n>> Linked List Size:",lRef.total_products())
print(">> Total Amount Pay:",lRef.total_amount)

# lRef.remove_product(Products(501, "Samsung A6", 3.8, "10% off", 13550, "February 10"))
# lRef.remove_product("Samsung A8")
# lRef.remove_product("Samsung LED")
# lRef.remove("IPhone 11")
#
# lRef.remove("Samsung A8")
# lRef.remove

lRef.head.show_product_info()
lRef.current.show_product_info()

lRef.remove_head()
lRef.remove_tail()

print()
lRef.head.show_product_info()
lRef.current.show_product_info()
# print("\nAfter removing product: ")
# # print("\nForward Move:")
# lRef.move_forward()
# print("\nBackward Move: ")
# lRef.move_backward()
#
# print("\n>> Linked List Size:",lRef.total_products())
# print(">> Total Amount Pay:",lRef.total_amount)