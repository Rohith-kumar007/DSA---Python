class queue:
    def __init__(self):
        self.arr=[]

    def enrear(self,val):
        return self.arr.append(val)

    def derear(self):
        return self.arr.pop()

    def enfront(self,val):
        return self.arr.insert(0,val)

    def defront(self):
        return self.arr.pop(0)

    def rearpeek(self):
        return self.arr[-1]

    def frontpeek(self):
        return self.arr[0]

    def display(self):
        print(len(self.arr))

res=queue()
n=int(input())
for i in range(n):
    oper=input().split()
    if len(oper)>=2:
        operation=oper[0]
        val=int(oper[1])

    else:
        operation=oper[0]

    if operation=='append':
        r=res.enrear(val)

    elif operation=='appendleft':
        res.enfront(val)

    elif operation=='pop':
        r=res.derear()
        print(r)

    elif operation=='popleft':
        r=res.defront()
        print(r)

    elif operation=='peek':
        r=res.rearpeek()
        print(r)

    elif operation=='peekleft':
        r=res.frontpeek()
        print(r)

    elif operation=='size':
        res.display()
