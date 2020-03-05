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

class Tree:

    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    def append_product(self, node, prd_object):

        if node is None:
            node = Tree()
            node.root = prd_object

            return node

        if prd_object.price <= node.root.price:
            node.left = self.append_product(node.left, prd_object)
        else:
            node.right = self.append_product(node.right, prd_object)

        return node

    def pre_order(self, node):
        if node is not None:
            node.root.show_product_info()
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        if node is not None:
            self.pre_order(node.left)
            node.root.show_product_info()
            self.pre_order(node.right)

    def post_order(self, node):
        if node is not None:
            self.pre_order(node.left)
            node.root.show_product_info()
            self.pre_order(node.right)

    def show_data(self):
        temp = self.root
        print("In order")
        self.pre_order(temp)
        print("Pre order")
        self.in_order(temp)
        print("post order")
        self.post_order(temp)

tRef = Tree()

tRef.root = tRef.append_product(None, Products(101, "IPhone 11", 4.5, "30% off", 14260, "January 24"))

tRef.append_product(tRef.root, Products(201, "IPhone Xs", 4.3, "25% off", 20410, "January 25"))
tRef.append_product(tRef.root, Products(301, "Samsung A10", 3.5, "20% off", 15620, "January 15"))
tRef.append_product(tRef.root, Products(401, "Samsung A8", 4.2, "15% off", 13260, "February 15"))
tRef.append_product(tRef.root, Products(501, "Samsung A6", 3.8, "10% off", 13550, "February 10"))

tRef.show_data()