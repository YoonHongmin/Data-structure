class DNode:
    def __init__(self,elem,prev=None,next=None): # 두개의 링크 prev, next
        self.data = elem
        self.prev = prev
        self.next = next
class DoublyLinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None    # 초기에는 양단 모두 None으로 설정 ( 비어있음 )
    def isEmpty(self) : return self.front == None
    def clear(self) : self.front = self.rear = None
    def size(self) :
        if self.isEmpty() : return 0
        else :  # 비어있지 않으면
            count = 1
            node = self.front.next # node는 front가 가리키는 링크필드부터 시작 
            while not node == self.rear: # rear에 도착하면 반복문 종료
                node = node.next   # 다음 노드
                count += 1
            print(self.front.data, self.rear.data)
            return count
    def display(self,msg='LinkedDeque: '):
        print(msg, end= '')
        node = self.front
        while not node == None:
            print(node.data, end=' ')
            node = node.next
        print()
    def addFront(self,item) :
        node = DNode(item,None,self.front)
        if self.isEmpty() :
            self.front = self.rear = node
        else :
            self.front.prev = node
            self.front = node
    def addRear(self,item) :
        node = DNode(item,self.rear,None)
        if self.isEmpty():
            self.front = self.rear = node
        else :
            self.rear.next = node
            self.rear = node
    def deleteFront(self) :
        if not self.isEmpty() :
            data = self.front.data  # 삭제할 데이터 저장
            self.front = self.front.next    # 노드 삭제
            if self.front == None : # 삭제했는데 더이상 데이터가 없으면 (삭제 후 노드가 한개뿐이면)
                self.rear = None   # rear도 None
            else :
                self.front.prev = None
            return data
    def deleteRear(self) :
        if not self.isEmpty() :
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None :
                self.front = None
            else :
                self.rear.next = None
            return data

