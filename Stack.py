class Stack:
    def __init__(self):
        self.items=[]

    def push(self,data):
        self.items.insert(0,data)

    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items==[]
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return (self.items)