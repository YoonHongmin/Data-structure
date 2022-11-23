class Node:
    def __init__(self,elem,next=None):
        self.data = elem
        self.link = next 
class CircularLinkedQueue:
    def __init__(self):
        self.tail = None    # tail: 유일한 데이터
    def isEmpty(self): return self.tail == None
    def clear(self) : self.tail = None
    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data  # tail이 링크하는, 즉 front(tail.link)의 data 반환
    def enqueue(self,item):
        node = Node(item,None)  # item을 데이터로 가지고, link가 None인 node를 생성
        if self.isEmpty():  # 큐가 비어있다면
            node.link = node    # node의 링크는 자기 자신을 가리킴
            self.tail = node    # tail은 노드를 가리킴
        else :
            node.link = self.tail.link  #노드의 링크에 tail이 가리키는 링크를 넣음 
            self.tail.link = node   # self.tail이 가리키고 있던 링크, 즉 삽입하려는 노드 before노드가 새로 삽입된 node를 가리킴
            self.tail = node    # tail은 새로 삽입된 node를 가리킴
    def dequeue(self):
        if not self.isEmpty():
            data = self.tail.link.data  # tail이 가리키고있는 링크필드의 데이터 (삭제할 노드의 데이터)
            if self.tail.link == self.tail :    # 큐가 하나의 항목을 가지면 (자신이 자신을 가리키면)
                self.tail = None
            else :
                self.tail.link = self.tail.link.link    # tail이 가리키고있는 링크필드가 가리키는 링크필드를 가리킴
            return data
    def size(self):
        if self.isEmpty() : return 0
        else :  # 비어있지 않으면
            count = 1
            node = self.tail.link # node는 tail이 가리키는 링크필드 ( front )부터 출발
            while not node == self.tail: # tail에 도착하면 반복문 종료
                node = node.link   # 다음 노드
                count += 1
            return count
    def display(self,msg='CircularLinkedQueue: '):
        print(msg, end= '')
        if not self.isEmpty():
            node = self.tail.link
            while not node == self.tail:
                print(node.data, end=' ')
                node = node.link
            print(node.data, end='')
        print()
q = CircularLinkedQueue()
