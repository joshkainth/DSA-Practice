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
# class Number:
#     def __init__(self, data):
#         self.data = data
#
#     def show_number(self):
#         print(self.data)

class TreeNode:
    def __init__(self):
        self.object = None
        self.left = None
        self.right = None

    def show_node(self):
        self.object.show_product_info()

class Tree:
    # root = None
    def __init__(self):
        self.root = None

    def append_product(self, node, prd_object):

        if node is None:
            node = TreeNode()
            node.object = prd_object
            # print("{} of [TreeNode]: {}".format(node.object.data, node.__dict__))
            return node

        if prd_object.price < node.object.price:
            node.left = self.append_product(node.left, prd_object)
        else:
            node.right = self.append_product(node.right, prd_object)

        return node

    def pre_order(self, prd_object):
       if prd_object is not None:
           prd_object.object.show_product_info()
           self.pre_order(prd_object.left)
           self.pre_order(prd_object.right)

    def in_order(self, prd_object):
        if prd_object is not None:
            self.in_order(prd_object.left)
            prd_object.object.show_product_info()
            self.in_order(prd_object.right)

    def post_order(self, prd_object):
        if prd_object is not None:
            self.post_order(prd_object.left)
            self.post_order(prd_object.right)
            prd_object.object.show_product_info()

    def show_tree(self):
        temp = self.root
        print("Pre-order")
        self.pre_order(temp)
        print("In-order")
        self.in_order(temp)
        print("Post-Order")
        self.post_order(temp)
        print()

    def minimum_value(self, prd_object):
        if prd_object is not None:
            if prd_object.left is not None:
                prd_object.object.show_product_info()

            self.minimum_value(prd_object.left)
        # temp.show_product_info()

    def maximum_value(self, prd_object):
        while prd_object.right is not None:
            prd_object = prd_object.right

        prd_object.object.show_product_info()
        #
        # temp.show_product_info()

    def max_value(self, prd_object):
        if prd_object is not None:
            if prd_object.right is not None:
                prd_object.object.show_product_info()

            self.maximum_value(prd_object.right)

    def search_product(self, prd_price, temp):
        element_found = True

        # if prd_price == node.object.price:
        #     node.object.show_product_info()
        #
        # if prd_price <= node.object.price:
        #     self.search_product(prd_price, node.left)
        # else:
        #     self.search_product(prd_price, node.right)

        while temp.object.price is not prd_price:
            if prd_price <= temp.object.price:
                temp = temp.left
            elif prd_price > temp.object.price:
                temp = temp.right
            else:
                element_found = False

        # temp.object.show_product_info()
        if element_found is False:
            print("Element Not Found")
        else:
            temp.object.show_product_info()

    def search(self, node, prd_price):
        if node.object.price == prd_price:
            node.object.show_product_info()
            return node

        if prd_price <= node.object.price:
            return self.search(node.left, prd_price)
        else:
            return self.search(node.right, prd_price)


tRef = Tree()

tRef.root = tRef.append_product(None, Products(101, "IPhone 11", 4.5, "30% off", 14260, "January 24"))

tRef.append_product(tRef.root, Products(201, "IPhone Xs", 4.3, "25% off", 20410, "January 25"))
tRef.append_product(tRef.root, Products(301, "Samsung A10", 3.5, "20% off", 15620, "January 15"))
#
tRef.append_product(tRef.root, Products(401, "Samsung A8", 4.2, "15% off", 13260, "February 15"))
tRef.append_product(tRef.root, Products(501, "Samsung A6", 3.8, "10% off", 13550, "February 10"))

# tRef.root = tRef.append_product(None, Number(50))
#
# tRef.append_product(tRef.root, Number(40))
# tRef.append_product(tRef.root, Number(30))
# tRef.append_product(tRef.root, Number(80))
# tRef.append_product(tRef.root, Number(90))
# tRef.append_product(tRef.root, Number(140))
# tRef.append_product(tRef.root, Number(55))
# tRef.append_product(tRef.root, Number(45))


# tRef.pre_order(tRef.root)
tRef.show_tree()
# print("Root Element: ",tRef.root.show_product_info())
print("Minimum Price: ", end="")
tRef.minimum_value(tRef.root)

print("Maximum Price: ", end="")
tRef.maximum_value(tRef.root)
# tRef.max_value(tRef.root)

# tRef.search_product(15620, tRef.root)
# tRef.search_product(12260, tRef.root)

tRef.search(tRef.root, 15620)
tRef.search(tRef.root, 12260)