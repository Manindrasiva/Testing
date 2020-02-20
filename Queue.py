class QueueImpl:
    def __init__(self, capcity):
        self.rear =self.fornt=self.size=0
        self.Q= [None] *capcity
        self.Capcity=capcity

    def isFull(self):
        return self.size == self.Capcity

        # Queue is empty when size is 0

    def isEmpty(self):
        return self.size == 0

    def Enqueue(self, data):
        self.Q[self.rear] = data
        self.rear = (self.rear + 1)
        self.size=self.size+1

    def deQueue(self):
        print("deleted item", self.Q[self.fornt])
        self.fornt = (self.fornt + 1)

    def print(self):
        return self.Q



