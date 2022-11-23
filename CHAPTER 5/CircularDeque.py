MAX_QSIZE = 10
class Stack :
    def __init__(self):self.top = []
    def isEmpty(self): return len(self.top) == 0
    def size(self):return len(self.top)
    def clear(self):self.top=[]
    def push(self,item):
        self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
    def __str__(self):
        return str(self.top[::-1])

class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE
    def isEmpty(self): return self.front == self.rear
    def isFull(self): return self.front ==(self.rear+1)%MAX_QSIZE
    def clear(self) : self.rear == self.front
    def enqueue(self,item):
        if not self.isFull():
            self.rear = (self.rear+1)%MAX_QSIZE
            self.items[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%MAX_QSIZE
            return self.items[self.front]
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)%MAX_QSIZE]
    def size(self):
        return (self.rear-self.front+MAX_QSIZE)%MAX_QSIZE
    def __str__(self):
        out = []
        if self.rear > self.front :
            out = self.items[self.front+1:self.rear+1]
        else :
            out = self.items[self.front+1:MAX_QSIZE] + self.items[0:self.rear+1]
        return "[f = %s , r = %s]"%(self.front,self.rear) + str(out)
    
class CircularDeque(CircularQueue):
    def __init__(self):
        super().__init__()
    def addRear(self, item) : 
        self.enqueue(item)
    def deleteFront(self):
        return self.dequeue()
    def getFront(self): 
        return self.peek()
    def addFront(self, item) :
        if not self.isFull():
            self.items[self.front] = item
            self.front = self.front-1
            if self.front < 0:
                self.front = MAX_QSIZE-1
    def deleteRear(self) :
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = self.rear-1
            if self.rear < 0 :
                self.rear = MAX_QSIZE-1
            return item
    def getRear(self) :
        if not self.isEmpty():
            return self.items[self.rear]

dq = CircularDeque()
s = Stack()
for i in range(1,9):
    dq.addRear(i)
print(dq)

for i in range(1,9):
    s.push(dq.deleteFront())
print(s)

for i in range(1,9):
    dq.addRear(s.pop())
print(dq)