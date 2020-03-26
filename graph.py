import matplotlib.pyplot as plt
import networkx
import string

# Undirected Graph
# Facebook Use Case

# User in Graph Data Structure is one of the Vertices/Nodes in Graph
class User:

    def __init__(self, uid, name, phone, email):
        self.uid = uid
        self.name = name
        self.phone = phone
        self.email = email

    def getUserDetails(self):
        return "{}. {} | {} | {}".format(self.uid, self.name, self.phone, self.email)

    def get_name(self):
        return self.name

# Consider as Graph Data Structure
class FaceBook:

    def __init__(self):
        self.users = dict()
        print(">> FaceBook Graph Created")
        print(">> users as of now:", self.users, "size:", len(self.users))

    # UnDirected Graph, we will add both users to each others adjacency list
    def connectUser(self, u1, u2):

        # We are checking if users exist as key in dictionary or not
        # if not, add the key and let the value be a list -> friendList
        if u1 not in self.users:
            self.users[u1] = []

        if u2 not in self.users:
            self.users[u2] = []

        # Add the Users in the adjacency list | FriendList of each other
        self.users[u1].append(u2)
        self.users[u2].append(u1)


    def printUsers(self):
        print(self.users)
        print(">> Total Users:", len(self.users))

    def printUsersWithFriendList(self):
        # Fetch all the keys from dictionary
        keys = self.users.keys()

        for key in keys:
            print(key.getUserDetails())
            print("Friend List:")
            friendList = self.users[key]
            for friend in friendList:
                print(friend.getUserDetails())

            print("*****************")
            print()

    def __str__(self):
        return self.name

    def create_graph(self):
        friends = networkx.Graph()
        keys = self.users.keys()
        nodeLists = [key.name for key in keys]

        for key in keys:
            # friends.add_node(key.name)
            for connection in self.users[key]:
                friends.add_edge(key.name, connection.name)

        pos = networkx.circular_layout(friends)
        networkx.draw_circular(friends, with_labels=True)
        plt.show()


def main():

    user1 = User(1, "John", "98765 90909", "john@example.com")
    user2 = User(2, "Jennie", "99887 67567", "jennie@example.com")
    user3 = User(3, "Fionna", "90909 87876", "fionna@example.com")
    user4 = User(4, "Dave", "98760 09876", "dave@example.com")
    user5 = User(5, "Kia", "99778 88990", "kia@example.com")
    user6 = User(6, "Leo", "98012 12345", "leo@example.com")
    # user7 = User(7, "Jack", "98012 12345", "jack@example.com")


    graph = FaceBook()

    graph.connectUser(user1, user2)
    graph.connectUser(user1, user3)
    graph.connectUser(user2, user4)
    graph.connectUser(user3, user4)
    graph.connectUser(user3, user5)
    graph.connectUser(user4, user5)
    graph.connectUser(user5, user6)


    graph.printUsers()

    print("~~~~~~~~~~~~")

    graph.printUsersWithFriendList()

    graph.create_graph()


if __name__ == '__main__':
    main()