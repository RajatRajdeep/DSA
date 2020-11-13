import sys

class Queue:
    def __init__(self):
        self.arr = []

    def enqueue(self, val):
        self.arr.append(val)

    def dequeue(self):
        if len(self.arr)>1:
            print("Deleted item from Queue : "+self.arr.pop(0))
        else:
            print("Delete operation can't be performed on Empty Queue")

    def print(self):
        print(self.arr)

if __name__ == "__main__":
    q = Queue()

    while True:
        operation = input('Enter E/e to Enqueue, D/d to Dequeue, P/p to print, and Q/q to Exit : ')
        if operation=='E' or operation=='e':
            item = input('Enter item value :')
            q.enqueue(item)
        elif operation=='D' or operation=='d':
            q.dequeue()
        elif operation=='Q' or operation=='q':
            sys.exit()
        elif operation=='P' or operation=='p':
            q.print()