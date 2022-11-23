class Node:
    def __init__(self,elem,next=None):
        self.data = elem
        self.link = next    # 이름이 같아도 self.link는 데이터 멤버 , link는 매개변수이므로 문제없음
class Linkedlist:  # 연결 리스트
    def __init__(self):
        self.head = None
        
    def isEmpty(self): return self.head == None # head이 가르키는것이 None이면 공백
    def clear(self): self.head == None # 초기화

    def insert(self,pos,elem):
        before = self.getNode(pos-1)    # 삽입하고싶은 노드 바로 전 노드를 찾아야함
        if before == None : # 맨 앞에 삽입하는 경우
            self.head = Node(elem,self.head)   # 맨 앞 노드를 새로운 노드를 생성해 가리키도록 함 head(맨 앞)은 삽입한 데이터를 가리킴
        else :
            node = Node(elem,before.link)   # 삽입하고싶은 데이터를 가리키는 노드를 생성, 그 노드는 before가 가리키던 노드 ( 앞 노드 )를 가리킴
            before.link = node  # before 노드가 새로 삽입한 데이터를 가리키도록 함
    def delete(self,pos):   # before 노드가 삭제할 노드 다음 노드를 가리키도록 하면 됨
        before = self.getNode(pos-1)    # before 노드를 찾음
        if before == None:  # 시작노드이면
            if self.head is not Node:   # 공백이 아니라면 ( 빈 리스트가 아니라면 )
                self.head = self.head.link  # self.head는 head가 가리키는 링크( 다음 노드 )
        elif before.link != None :
            before.link = before.link.link  # before의 링크를 before가 기존에 가리키던 링크의 링크를 가리킴 ( 다음 노드 )

    def peek(self): # 시작노드의 데이터를 반환
        if not self.isEmpty():
            return self.head.data
    def size(self):
        node = self.head
        count = 0
        while not node == None: # node가 None이 아닐때 까지, 마지막 노드 까지
            node = node.link   # 다음노드
            count +=1
        return count
    def display(self, msg='LinkedStack: ') :
        print(msg, end=' ')
        node = self.head # 시작 노드를 저장할 변수(node)
        while not node == None:
            print(node.data, end='->')
            node = node.link # 노드에 link된(다음) 노드를 가리킴
        print('None')

    def getNode(self,pos) : # 시간복잡도 O(n) , pos번째 항목을 반환
        if pos < 0 : return None
        node = self.head
        while pos > 0 and node is not None:
            node = node.link
            pos -= 1    # pos의 값을 하나씩 줄여나감 ( 가까워진다고 이해 )
        return node # 최종 노드 반환
    def getEntry(self,pos):
        node = self.getNode(pos)    # 노드를 반환받고
        if node is None : return None
        else : return node.data # 노드의 데이터를 반환
    def replace(self,pos,elem):
        node = self.getNode(pos)
        if node is not  None : node.data = elem
    def find(self,val):
        node = self.head
        while node != None:
            if node.data == val : return node
            node = node.link
        return node

s = Linkedlist()
s.insert(0,10)
s.insert(1,30)
s.insert(2,130)
s.display()

