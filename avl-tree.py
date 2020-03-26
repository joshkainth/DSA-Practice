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

    def rotate_left(self):
        temp = self.root.right
        self.root.right = temp.left
        temp.left = self.root
        self.root = temp

    def rotate_right(self):
        temp = self.root.left
        self.root.left = temp.right
        temp.right = self.root
        self.root = temp

tRef = Tree()

tRef.root = tRef.append_product(None, Products(101, "IPhone 11", 4.5, "30% off", 80000, "January 24"))

tRef.append_product(tRef.root, Products(201, "IPhone Xs", 4.3, "25% off", 50000, "January 25"))
tRef.append_product(tRef.root, Products(301, "Samsung A10", 3.5, "20% off", 20000, "January 15"))

print("Before Rotation | Pre-orderTraversal")
tRef.pre_order(tRef.root)

print("Left Rotation")
tRef.rotate_right()

print("After Rotation | Pre-order Traversal")
tRef.pre_order(tRef.root)