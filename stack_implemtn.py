class Stack(object):

    def __init__(self):
        self.items = []

    def inEmpty(self):
        return self.items == []

    def push(self,item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(Self):
        return len(self.items)    

s = Stack()

# print s.inEmpty()

s.push('two')
print s.peek()
s.push(True)

print s.peek()

s.push(1)

print s.peek()

#print s.inEmpty()

s.pop()

print s.peek()