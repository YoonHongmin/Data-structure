class PriorityQueue :   # 정렬되지 않은 배열을 이용한 우선순위 큐의 구현
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return len(self.items) == 0
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self) :
        highest = self.findMaxIndex()
        if highest is not None :
            return self.items.pop(highest)
    def peek(self) :
        highest = self.findMaxIndex()
        if highest is not None :
            return self.items[highest]
    def findMaxIndex(self):
        if self.isEmpty() : return None
        else :
            highest = 0
            for i in range(1,self.size()):
                if self.items[i] > self.items[highest]:
                    highest = i
            return highest

q = PriorityQueue()
q.enqueue(34)
q.enqueue(18)
q.enqueue(45)
q.enqueue(7)
print("PQUEUE: ",q.items)
print(q.dequeue())
print(q.dequeue())