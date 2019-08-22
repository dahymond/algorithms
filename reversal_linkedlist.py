class Node(object):

    def __init__(self,value):

        self.value = value
        self.nextnode = None

    def reversal(head):
        current = head
        previous = None
        nextnode = None
        

        while current != None:
            nextnode = current.nextnode
            
            current.nextnode = previous

            previous = current
            current = nextnode

        return previous    