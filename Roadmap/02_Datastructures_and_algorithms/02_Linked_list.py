# lesser known cousin of list
# ordered collection of objects
# store references as part of their own elements
# Each element of a linked list is called a node;
#     1. Data: value to be stored in the node
#     2. Next: reference to the next node

# usecases;
# 2. lifecycle management of an OS applications
# 1. implement queues, or stacks as well as graphs

# Queues: elements retrieved in first-in-first-out(FIFO) approach
from collections import deque
queue = deque()  #-> deque([])
queue.append("Mary")  #-> deque(['Mary'])
queue.append("John")  #-> deque(['Mary', 'John'])
queue.popleft()  #-> deque(['John'])
queue.popleft()  #-> deque([])

# Stacks: elements retrieved in last-in-first-out(LIFO) approach
from collections import deque
stack = deque()  #-> deque([])
stack.appendleft("Mary")  #-> deque(['Mary'])
stack.appendleft("John")  #-> deque(['John', 'Mary'])
stack.popleft()  #-> deque(['Mary'])
stack.popleft()  #-> deque([])

# Graphs: show the relationship between objects or represent networks



#  Implementing own Linked list 
class Node:
    def __init__(self, dataf):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
      
node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node1.next = node2
node2.next = node3
l1 = LinkedList()
l1.head = node1
print(l1)  #-> "A -> B -> C -> None"



# edit LinkedList class for fastly add data and add traverse function
# traverse is a fancy name for iteration
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data
      

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def add_first(self, node):  # inserting at the beginning
        node.next = self.head
        self.head = node

    def add_last(self, node):  # inserting at the end
        if self.head is None:
            self.head = node
            return
        for current_node in self:  # traverse list until reach last
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):  # insert after an existing node
        if self.head is None:
            raise Exception("List is empty")
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("Node with data '%s' not found" % target_node_data)  

    def add_before(self, target_node_data, new_node):  # insert before an existing node
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        raise Exception("Node with '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Excempiton("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Excemption("Node with '%s' not found" % target_node_data)

  
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def __repr__(self):  # string representation of an object that is as unambiguous as possible. Used to recreate an object.
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


llist = LinkedList(["a", "b", "c", "d", "e"])
print(llist)  # a -> b -> c -> d -> e -> None

for node in llist:  # __iter__ function make the LinkedList iterable. making possible the use of for loop
    print(node)  # a, b, c, d, e
  
llist.add_first(Node("Z"))  # Z -> a -> b -> c -> d -> e -> None
llist.add_last(Node("X"))  # Z -> a -> b -> c -> d -> e -> X -> None
llist.add_after("Z", Node("2"))  # Z -> 2 -> a -> b -> c -> d -> e -> X -> None
llist.add_before("X", Node("1"))  # Z -> 2 -> a -> b -> c -> d -> e -> 1 -> X -> None
llist.remove_node("c")  # Z -> 2 -> a -> b -> d -> e -> 1 -> X -> None



# Doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # reference next node
        self.previous = None  # reference previous node



# Circular linked list
# last node point to head of the list instead on None
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def print_list(self, starting_point=None):
        nodes = []
        for node in self.traverse(starting_point):
            nodes.append(str(node))
        print(" -> ", join(nodes))
