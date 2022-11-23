
MAX_QSIZE = 10
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

q = CircularQueue()
print(q)
q.enqueue(1)
q.enqueue(2)
print(q)
