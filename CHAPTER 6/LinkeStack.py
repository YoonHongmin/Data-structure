class Node:
    def __init__(self,elem,link=None):
        self.data = elem
        self.link = link    # 이름이 같아도 self.link는 데이터 멤버 , link는 매개변수이므로 문제없음
class LinkedStack:  # 스택을 이용한 연결 리스트
    def __init__(self):
        self.top = None
        
    def isEmpty(self): return self.top == None # top이 가르키는것이 None이면 공백
    def clear(self): self.top == None # 초기화
    def push(self,item):
        n = Node(item,self.top) # self.top 즉 top은 시작 노드이므로 n의 링크가 시작노드를 가리키도록 함(원래 top이 가리키던 노드)
        self.top = n    # top이 n을 가리키도록 함 top = n
    def pop(self):
        if not self.isEmpty():
            n = self.top # 새로운 변수 n이 시작 노드(top)를 가리키게 함
            self.top = n.link  # top이 다음 노드를 가리키도록 함 n.link는 첫번째 노드가 가리키는 링크
            return n.data   # n의 데이터를 반환 함
    # 파이썬은 어떤 객체를 참조하는 변수가 하나도 없으면 그 객체는 자동으로 삭제
    def peek(self): # 시작노드의 데이터를 반환
        if not self.isEmpty():
            return self.top.data
    def size(self):
        node = self.top
        count = 0
        while not node == None: # node가 None이 아닐때 까지, 마지막 노드 까지
            node = node.link   # 다음노드
            count +=1
        return count
    def display(self, msg='LinkedStack: ') :
        print(msg, end=' ')
        node = self.top # 시작 노드를 저장할 변수(node)
        while not node == None:
            print(node.data, end=' ')   # 가장 최근에 삽입된 데이터 부터 출력
            node = node.link # 노드에 link된(다음) 노드를 가리킴
        print()

odd = LinkedStack()
even = LinkedStack()
for i in range(10):
    if i%2 ==0 : even.push(i)
    else : odd.push(i)
odd.display()
even.display()
for i in range(2): even.pop()
for i in range(3): odd.pop()
odd.display()
even.display()