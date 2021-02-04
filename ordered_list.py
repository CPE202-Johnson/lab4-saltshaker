class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Head and tail used to keep track of the front and back of list'''
        self.head = None
        self.tail = None

    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        if self.head == None:
            return True
        else:
            return False

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance'''
        if self.search(item):      # Item is in the list
            return False
            
        # Item is not in list
        if self.is_empty():             # List is empty so head and tail need to be set
            self.head = Node(item)
            self.tail = self.head
        elif item < self.head.item:     # Item is smaller than head
            temp = Node(item)
            self.head.prev = temp
            temp.next = self.head
            self.head = temp
        elif self.tail.item < item:     # Item is larger than tail
            temp = Node(item)
            self.tail.next = temp
            temp.prev = self.tail
            self.tail = temp
        else:                           # Item should go somewhere inside the list
            current = self.head
            while current.item < item:  # Move to the node that will be to the right of the Node being added
                current = current.next
            temp = Node(item)
            temp.next = current
            temp.prev = current.prev
            current.prev.next = temp
            current.prev = temp  
        return True
            

    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list) 
          returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        itemIndex = self.index(item)
        if itemIndex == None:       # Item isn't in the list
            return False
            
        if self.head == self.tail:  # Special case for 1 Node in list
            self.head = None
            self.tail = self.head
            return True
            
        if item == self.head.item:      # Special case for removing head
            self.head.next.prev = None
            self.head = self.head.next
        elif item == self.tail.item:    # Special case for removing tail
            self.tail.prev.next = None
            self.tail == self.tail.prev
        else: 
            current = self.head
            i = 0
            while i < itemIndex:        # Move to node that corresponds to the index
                current = current.next
                i += 1
            
            current.prev.next = current.next
            current.next.prev = current.prev

        return True

    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        if self.search(item):
            i = 0
            current = self.head
            while current != None:      # Ends after tail has been checked
                if current.item == item:
                    break
                current = current.next
                i += 1
            return i
        else:                       # Item isn't in the list
            return None

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        if (index < 0) | (index >= self.size()):
            raise IndexError

        current = self.head
        i = 0
        while i < index:            # Move to node that corresponds with index
            current = current.next
            i += 1
        
        if self.head == self.tail:  # Special case for list of one Node
            self.head = None
            self.tail = self.head
        elif current == self.head:  # Speical case for popping head
            self.head = current.next
            self.head.prev = None
        elif current == self.tail:  # Special case for popping tail
            self.tail = current.prev
            self.tail.next = None
        else:
            current.prev.next = current.next    
            current.next.prev = current.prev
        return current.item

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        if self.is_empty():
            return False
            
        current = self.head
        return self.searchRecursive(current, item)      # Recursive helper function
        
    def searchRecursive(self, node, item):
        '''Recursive helper function
           inputs: Node and item
           outputs: bool'''
        # Stop cases
        if node == None:
            return False
        if node.item == item:
            return True
        if item < node.item:
            return False
        
        return False | self.searchRecursive(node.next, item)


    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        size = self.size()
        list = [None] * size        # Create list of needed size to avoid using append()
        i = 0
        current = self.head
        while i < size:
            list[i] = current.item
            current = current.next
            i += 1
        return list
        

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        size = self.size()
        rlist = [None] * size       # Create list of needed size to avoid using append()
        current = self.tail
        self.reversedListRecursive(rlist, current, 0)
        return rlist
        
    def reversedListRecursive(self, rlist, node, index):
        '''Recursive helper function
           inputs: list, node, int
           output: None since list is mutable'''
        if node == None:
            return
            
        rlist[index] = node.item
        self.reversedListRecursive(rlist, node.prev, index+1)

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        if self.is_empty():
            return 0
            
        current = self.head
        return self.sizeRecursive(current)
    
    def sizeRecursive(self, node):
        '''Recursive helper function
           inputs: node
           outputs: int'''
        if node == None:     # Current node is the tail
            return 0

        return self.sizeRecursive(node.next) + 1
