class node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def str(self):
        return self.data

class Queue:
    def __init__(self):
        self.rear=None
        self.front=None

    def enqueue(self,data):
        newnode=node(data)
        if self.rear is None:
            self.rear=newnode
            self.front=newnode
            self.rear.next=self.front
        else:
            self.rear.next=newnode
            self.rear=newnode
            self.rear.next=self.front
        print(f"{newnode.data} added to the queue")

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return
        removed=self.front.data
        
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
            self.rear.next=self.front

        print(f"{removed} is removed from the queue")

obj=Queue()
n=int(input())
for i in range(n):
    op=input().split()
    oper=op[0]
    st=' '.join(op[1:])

    if oper=='ENQUEUE':
        obj.enqueue(st)
    elif oper=='DEQUEUE':
        obj.dequeue()
