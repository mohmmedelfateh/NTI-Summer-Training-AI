class Queue:
    def __init__(self):
        self.list1 = []
        pass

    def insert_M(self, member):
        self.list1.insert(len(self.list1), member)

    def pop_M(self):
        if len(self.list1) > 0:
            self.list1.pop(0)
        else:
            raise Exception("Sorry, no member in Queue")

    def is_empty(self):
        if self.list1:
            return True
        else:
            raise Exception("The list is empty")

    def show_Q(self):
        return self.list1


class QueueV2(Queue):
    Arc_Q = {}

    def __init__(self, name, size):
        super().__init__()
        self.name = name
        self.size = size
        self.list1 = []
        QueueV2.Arc_Q[self.name] = self.list1

    def insert_Q(self, member):
        if len(self.list1) < self.size:
            self.list1.append(member)
        else:
            raise Exception('QueueOutOfRangeException')


P = QueueV2("P", 5)
K = QueueV2('K', 7)
L = QueueV2('L', 3)
P.insert_Q(5)
P.insert_Q(2)
P.insert_Q(4)
P.insert_Q(3)
P.insert_Q(3)
print(QueueV2.Arc_Q)
