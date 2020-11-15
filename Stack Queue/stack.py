import sys

class Stack:
    def __init__(self):
        self.arr = []

    def push(self, val):
        self.arr.append(val)

    def pop(self):
        if len(self.arr)>1:
            print("Poped item from Stack : "+self.arr.pop())
        else:
            print("Pop operation can't be performed on Empty Stack")

    def print(self):
        print(self.arr[::-1])

if __name__ == "__main__":
    s = Stack()

    while True:
        operation = input('Enter A/a to Push, D/d to Pop, P/p to print, and Q/q to Exit : ')
        if operation=='A' or operation=='a':
            item = input('Enter item value :')
            s.push(item)
        elif operation=='D' or operation=='d':
            s.pop()
        elif operation=='Q' or operation=='q':
            sys.exit()
        elif operation=='P' or operation=='p':
            s.print()