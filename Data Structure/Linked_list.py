class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def insert_head(self, newnode):
        if self.head is None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def insert_last_list(self, newnode):
        if self.head is None:
            self.head = newnode
        else:
            last_node = self.head
            while True:
                if last_node.next is None:
                    last_node.next = newnode
                    break
                else:
                    last_node = last_node.next

    def insert_index(self, newnode, index):
        if index == 0:
            newnode.next = self.head
            self.head = newnode
            return
        i = 0
        n = self.head
        while i < index - 1 and n is not None:
            n = n.next
            i = i + 1
        if n is None:
            raise Exception("You can't insert element here! :( ")
        else:
            newnode.next = n.next
            n.next = newnode

    def del_index(self, index):
        c_node = self.head
        if index == 0:
            self.head = c_node.next
            c_node = None
            return print('Deleted done')
        for i in range(index - 1):
            c_node = c_node.next
            if c_node is None:
                break
        if c_node is None:
            raise Exception("No element here! :( ")
        if c_node.next is None:
            raise Exception("No element here! :( ")
        next1 = c_node.next.next
        c_node.next = None
        c_node.next = next1
        print('Deleted done')

    def del_head(self):
        c_node = self.head
        self.head = c_node.next
        c_node.next = None
        return print('Deleted done')

    def del_last(self):
        if self.head is None:
            raise Exception("The list has no element to delete")

        c_node = self.head
        while c_node.next.next is not None:
            c_node = c_node.next
        c_node.next = None
        print('Deleted done')

    def print_node(self):
        c_nade = self.head
        if self.head is None:
            print("list is empty")

        while True:
            if c_nade is None:
                break
            else:
                print(c_nade.data)
                c_nade = c_nade.next
