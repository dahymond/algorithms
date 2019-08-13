class Stack(object):

    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def newPush(self, item):
        return self.items.append(item)

    def popItem(self):
        return self.items.pop()

    def peepItem(self):
        return self.items[len(self.items)-1]

    def stackSize(self):
        return len(self.items)



