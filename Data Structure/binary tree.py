class root:
    def __init__(self, data):
        self.root = data
        self.right = None
        self.left = None

    def insert_node(self, newdata):
        if self.root:
            if newdata < self.root:
                if self.left is None:
                    self.left = root(newdata)
                else:
                    self.left.insert_node(newdata)
            if newdata > self.root:
                if self.right is None:
                    self.right = root(newdata)
                else:
                    self.right.insert_node(newdata)

    def print_pre(self, root1):
        list1 = []
        if root1:
            list1.append(root1.root)
            list1 = list1 + self.print_pre(root1.left)
            list1 = list1 + self.print_pre(root1.right)

        return list1

    def print_post(self, root1):
        list1 = []
        if root1:
            list1 = list1 + self.print_post(root1.left)
            list1 = list1 + self.print_post(root1.right)
            list1.append(root1.root)
        return list1

    def print_in(self, root1):
        list1 = []
        if root1:
            list1 = list1 + self.print_in(root1.left)
            list1.append(root1.root)
            list1 = list1 + self.print_in(root1.right)
            #test
        return list1


n1 = root(9)
n1.insert_node(5)
n1.insert_node(6)
n1.insert_node(4)
n1.insert_node(8)
n1.insert_node(10)
print(n1.print_pre(n1))
print(n1.print_in(n1))
print(n1.print_post(n1))
