class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
        self.temp=None

    def insert_at_beginning(self,data):
        new_node=node(data)
        if self.head==None:
            self.head=new_node
            self.temp=new_node
        else:
            new_node.next=self.head
            self.head=new_node

    def insert_at_end(self,data):
        new_node=node(data)
        self.temp=self.head
        while self.temp.next!=None:
            self.temp=self.temp.next
        self.temp.next=new_node

    def display(self):
        self.temp=self.head
        if  self.head!=None:
            while self.temp!=None:
                print(self.temp.data, end=" ")
                self.temp=self.temp.next
            print()
        else:
            print("The list is empty.")


    def insert_after(self,x,y):
        self.temp=self.head
        while self.temp.next!=None:
            if self.temp.data==y:
                newnode=node(x)
                newnode.next=self.temp.next
                self.temp.next=newnode
                break
            else:
                self.temp=self.temp.next

    def delete_tail(self):
        self.temp=self.head
        while self.temp.next.next!=None:
            self.temp=self.temp.next
        self.temp.next=None

    def delete_node(self,x):
        self.temp=self.head
        if self.head.data==x:
            self.head=self.head.next
        while self.temp.next!=None:
            if self.temp.next!=None:
                if self.temp.next.data==x:
                    temp=self.temp.next.next
                    self.temp.next=temp
                else:
                    self.temp=self.temp.next

obj=SLL()
n=int(input())
for i in range(n):
    s=list(map(int,input().split(" ")))
    if s[0]==1:
        obj.insert_at_beginning(s[1])
    elif s[0]==2:
        obj.insert_at_end(s[1])
    elif s[0]==3:
        obj.insert_after(s[1],s[2])
    elif s[0]==4:
        obj.display()
    elif s[0]==5:
        obj.delete_tail()
    elif s[0]==6:
        obj.delete_node(s[1])
