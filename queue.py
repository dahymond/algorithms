class Queue(object):

    def __init__ (self):
        self.items = []

    def isEmpty(self):
        self.items = []

    def size(self):
        return len(self.items)    

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self, item):
        return self.items.pop()  

        








