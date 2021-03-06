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

    size = 0
    total_amount = 0

    def __init__(self):
        self.head = None
        self.current = None

    def append_product(self, product_object):

        LinkedList.size += 1
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

        LinkedList.size += 1
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

    def append_at_particular_position(self, product_object, product_name):

        LinkedList.size += 1
        LinkedList.total_amount += product_object.price

        product_object.next = None
        product_object.previous = None

        temp = self.head
        target = None

        while temp.next is not self.head:
            if temp.title == product_name:
                address1 = target
                address2 = temp

                target.next = product_object
                temp.previous = product_object

                product_object.next = address2
                product_object.previous = address1
                break

            target = temp
            temp = temp.next

    def remove_product(self, product_name):

        LinkedList.size -= 1

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

    def remove(self, product_name):

        temp = self.head            # temp -> current,  target -> previous
        target = None
        product_found = True

        while temp.next is not self.head:
            if temp.title == self.head.title == product_name:
                print("self.remove_head() function Called:")
                self.remove_head()
                break

            elif temp.title == product_name:
                print("Simple Remove function Called")
                LinkedList.size -= 1

                address1 = temp.next
                target.next = address1
                temp.next.previous = target

                LinkedList.total_amount -= temp.price
                del temp
                break

            elif temp.title == self.current.title == product_name:
                print("self.remove_tail() function Called:")
                self.remove_tail()
                break

            target = temp
            temp = temp.next


    def remove_head(self):
        LinkedList.size -= 1

        temp = self.head
        self.head = temp.next
        self.head.previous = self.current
        self.current.next = self.head

        LinkedList.total_amount -= temp.price

        del temp

    def remove_tail(self):
        LinkedList.size -= 1

        temp = self.current
        self.current = self.current.previous
        self.current.next = self.head
        self.head.previous = self.current

        LinkedList.total_amount -= self.current.price

        del temp

    def swap_data(self, prd1, prd2):
        temp_pid = prd1.pid
        temp_title = prd1.title
        temp_rating = prd1.rating
        temp_deal = prd1.deal
        temp_price = prd1.price
        temp_delivery_date = prd1.delivery_date

        prd1.pid = prd2.pid
        prd1.title = prd2.title
        prd1.rating = prd2.rating
        prd1.deal = prd2.deal
        prd1.price = prd2.price
        prd1.delivery_date = prd2.delivery_date

        prd2.pid = temp_pid
        prd2.title = temp_title
        prd2.rating = temp_rating
        prd2.deal = temp_deal
        prd2.price = temp_price
        prd2.delivery_date = temp_delivery_date

    def swap_product(self, prd1, prd2):
        print("Before: [prd1.title: {}] [prd1.next: {}] [prd1.previous: {}]".format(prd1.title, prd1.next, prd1.previous))
        print("Before: [prd2.title: {}] [prd2.next: {}] [prd2.previous: {}]".format(prd2.title, prd2.next, prd2.previous))

        prd1.previous.next = prd2
        prd2.next.previous = prd1

        prd1.next = prd2.next
        prd1.previous = prd2

        prd2.next = prd1
        prd2.previous = prd1.previous

        if prd1 == self.head:
            self.head = prd2

        if prd2 == self.current:
            self.current = prd1

        print("After: [prd1.title: {}] [prd1.next: {}] [prd1.previous: {}]".format(prd1.title, prd1.next, prd1.previous))
        print("After: [prd2.title: {}] [prd2.next: {}] [prd2.previous: {}]".format(prd2.title, prd2.next, prd2.previous))
        print()

    def bubble_sort(self):

        iTemp = self.head
        jTemp = self.head

        for i in range(0, LinkedList.size):
            for j in range(0, LinkedList.size-i-1):

                if jTemp.price > jTemp.next.price:
                    self.swap_product(jTemp, jTemp.next)

                jTemp = jTemp.next

            jTemp = self.head
            iTemp = iTemp.next

    def move_forward(self):
        temp = self.head
        for i in range(0, LinkedList.size):
            temp.show_product_info()
            temp = temp.next

    def move_backward(self):
        temp = self.current
        for i in range(0, LinkedList.size):
            temp.show_product_info()
            temp = temp.previous

    def total_products(self):
        return LinkedList.size

lRef = LinkedList()
lRef.append_product(Products(101, "IPhone 11", 4.5, "30% off", 75260, "January 24"))
lRef.append_product(Products(201, "IPhone Xs", 4.3, "25% off", 95410, "January 25"))
lRef.append_product(Products(301, "Samsung A10", 3.5, "20% off", 15620, "January 15"))

lRef.append_product(Products(401, "Samsung A8", 4.2, "15% off", 13260, "February 15"))
lRef.append_product(Products(501, "Samsung A6", 3.8, "10% off", 17550, "February 10"))

# lRef.append_at_beginning(Products(401, "Samsung A8", 4.2, "15% off", 13260, "February 15"))
# lRef.append_at_beginning(Products(501, "Samsung A6", 3.8, "10% off", 13550, "February 10"))

lRef.append_at_particular_position(Products(601, "Samsung LED", 4.2, "30% off", 30250, "February 15"), "IPhone Xs")
# Insertion with Name and it is done before that given name

print("\n>> Linked List: ", lRef.__dict__)
print("\nForward Move:")
lRef.move_forward()
#
print("\nBackward Move: ")
lRef.move_backward()

print("\n>> Linked List Size:",lRef.total_products())
print(">> Total Amount Pay:",lRef.total_amount)


print("After Sorting:")
lRef.bubble_sort()
lRef.move_forward()

# lRef.remove_product(Products(501, "Samsung A6", 3.8, "10% off", 13550, "February 10"))
# lRef.remove_product("Samsung A8")
# lRef.remove_product("Samsung LED")
# lRef.remove("IPhone 11")
#
# lRef.remove("Samsung A8")
# lRef.remove

# lRef.head.show_product_info()
# lRef.current.show_product_info()

# lRef.remove_head()
# lRef.remove_tail()
# #
# # print()
# # lRef.head.show_product_info()
# # lRef.current.show_product_info()
# print("\nAfter removing product: ")
# # print("\nForward Move:")
# lRef.move_forward()
# print("\nBackward Move: ")
# lRef.move_backward()
#
# print("\n>> Linked List Size:",lRef.total_products())
# print(">> Total Amount Pay:",lRef.total_amount)