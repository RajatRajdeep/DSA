import sys

class Node:
    def __init__(self, item):
        self.val = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        if self.head==None:
            self.head = Node(item)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(item)
        
    def print(self):
        node = self.head
        while node:
            print(node.val, end=" ")
            node = node.next

if __name__ == "__main__":
    l = LinkedList()
    while True:
        operation = input('Enter A/a to Add, P/p to print, and Q/q to Exit : ')
        if operation=='A' or operation=='a':
            item = input('Enter item value :')
            l.add(item)
        elif operation=='P' or operation=='p':
            l.print()
        elif operation=='Q' or operation=='q':
            sys.exit()