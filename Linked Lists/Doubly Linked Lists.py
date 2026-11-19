class DoublyNode:
    def __init__(self,val , next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)

Head = Tail = DoublyNode(1) # head and tail start hota ha
# print(tail)

#displaying elements
def display(Head):
    curr = Head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(" <-> ".join(elements))

display(Head)

#Inserting a node at beginnning-O(1)
def InsertAtBeginning(Head, Tail, val):
    new_node = DoublyNode(val, next=Head)
    Head.prev = new_node
    return new_node , Tail  

Head,Tail = InsertAtBeginning(Head, Tail, 5)
display(Head)


def InsertAtEnd(Head, Tail, val):
    new_node = DoublyNode(val, prev = Tail)
    Tail.next = new_node
    return Head,new_node
    


Head , Tail = InsertAtEnd(Head, Tail, 7)
display(Head)




























