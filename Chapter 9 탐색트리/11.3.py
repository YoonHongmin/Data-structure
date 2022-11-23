class BSTNode:
    def __init__(self,key,value):   # 생성자 : 키와 값을 받음
        self.key = key  # 키(key)
        self.value = value  # 값(value)
        self.left = None    # 왼쪽 자식에 대한 링크
        self.right = None   # 오른쪽 자식에 대한 링크
    
def inorder(n) :            
    if n is not None :
        inorder(n.left)         
        print(n.key, end=' ')   
        inorder(n.right)

def calc_height(n) :
    if n is None :                
        return 0
    hLeft = calc_height(n.left)      
    hRight = calc_height(n.right)   
    if (hLeft > hRight) :          
        return hLeft + 1
    else: 
        return hRight + 1
    
def count_node(n):
    if n is None :
        return 0
    else :
        return 1 + count_node(n.left) + count_node(n.right)

def search_bst(n,key):  # 이진탐색트리 탐색연산(순환)
    # n(Node)은 이진탐색트리의 root 부터 시작 , key는 찾고자 하는 값
    if n == None:
        return None
    elif key == n.key:  # n의 키 값과 동일하면 탐색 성공  
        return n
    elif key < n.key:
        return search_bst(n.left, key)  # 찾고자하는 값이 n의 key값보다 작으면 왼쪽 순환으로 서브트리 탐색 
    else:
        return search_bst(n.right, key) # 찾고자하는 값이 n의 key값보다 크면 오른쪽 순환으로 서브트리 탐색 

def search_bst_iter(n, key):    # 이진탐색트리 탐색연산(반복)
    while n != None :   # n이 None이 아닐 때 까지
        if key == n.key:    # n의 키 값과 동일하면 탐색 성공
            return n
        elif key < n.key:   # 찾고자하는 값이 n의 key값보다 작으면 왼쪽 서브트리로 이동
            n = n.left
        else:               # 찾고자하는 값이 n의 key값보다 크면 오른쪽 서브트리로 이동
            n = n.right
    return None # 노드를 다 돌았는데 찾는 키에 해당하는 노드가 없음

def search_value_bst(n, value) :
    if n == None : return None
    elif value == n.value:               
        return n
    res = search_value_bst(n.left, value)    
    if res is not None :               
       return res                     
    else :                           
       return search_value_bst(n.right, value)

def search_max_bst(n) :     # 최대 값 노드 탐색
    if n.right == None : return n
    else :
        return search_max_bst(n.right)

def search_min_bst(n) :     # 최소 값 노드 탐색
    if n.left == None : return n
    else :
        return search_min_bst(n.left)

def insert_bst(r, n) :
    while(True):
        if n.key < r.key :
            if r.left is None :
                r.left = n
                return True
            else :
                r = r.left
        elif n.key > r.key :
            if r.right is None :
                r.right = n
                return True
            else :
                r = r.right
        else :
            return False
    
def delete_bst_case1 (parent, node, root) : # 단말 노드의 삭제
    if parent is None :     # 삭제할 노드가 root 노드이면 ( 부모가 None )
        root = None     # 공백 트리가 됨
    else :
        if parent.left == node :    # 삭제할 노드가 부모의 왼쪽 자식이면
            parent.left = None      # 부모의 왼쪽 노드를 None
        else :                      # 삭제할 노드가 부모의 오른쪽 자식이면
            parent.right = None     # 부모의 오른쪽 노드를 None
    return root

def delete_bst_case2 (parent, node, root) : # 자식이 하나인 노드 삭제
    if node.left is not None :  # 삭제할 도느가 왼쪽 자식만 가지면
        child = node.left   # child는 왼쪽 자식
    else :                      # 삭제할 도느가 오른쪽 자식만 가지면 
        child = node.right   # child는 오른쪽 자식

    if node == root :   # 없애려는 노드가 root 노드이면
        root = child    # chile가 root 노드가 됨
    else :
        if node is parent.left :    # 삭제할 노드가 부모의 왼쪽 자식
            parent.left = child     # 부모의 왼쪽 노드를 변경
        else :                      # 삭제할 노드가 부모의 오른쪽 자식
            parent.right = child    # 부모의 오른쪽 노드를 변경
    return root

def delete_bst_case3 (parent, node, root) : # 자식이 두개인 노드 삭제
    succp = node    # 후계자의 부모 노드   
    succ = node.right   # 후계자의 노드
    while (succ.left != None) :
        succp = succ
        succ = succ.left

    if (succp.left == succ) :   # 후계자가 왼쪽 자식이면
        succp.left = succ.right     # 후계자의 오른쪽 자식 연결
    else :                      # 후계자가 오른쪽 자식이면
        succp.right = succ.right    # 후계자의 왼쪽 자식 연결
    node.key = succ.key
    node.value = succ.value
    node = succ
    return root

def delete_bst(root, key) :
    if root == None : return None
    parent = None
    node = root
    while node != None and node.key !=key :
        parent = node
        if key < node.key : node = node.left
        else : node = node.right

    if node == None : return None    
    if node.left == None and node.right == None :
        root = delete_bst_case1(parent, node, root)
    elif node.left == None or node.right == None :
        root = delete_bst_case2(parent, node, root)
    else :
        root = delete_bst_case3(parent, node, root)
    return root

class PriorityQueue :                 
    def __init__ (self):         
        self.root = None         

    def isEmpty (self): return self.root == None   
    def clear(self): self.root = None              
    def size(self): return count_node(self.root)   

    def search(self, key): return search_bst(self.root, key)
    def searchValue(self, key): return search_value_bst(self.root, key)
    def peek(self): return search_max_bst(self.root)
    def findMin(self): return search_min_bst(self.root)

    def enqueue(self, key, value=None):   
        n = BSTNode(key, value)          
        if self.isEmpty() :              
           self.root = n
           return n
        else :                        
           insert_bst(self.root, n)  

    def dequeue(self):
            k = search_max_bst(self.root) 
            delete_bst(self.root, k.key)   

    def display(self, msg = 'BSTMap :'):
        print(msg, end='')
        inorder(self.root)
        print()

pQ = PriorityQueue()
print("[우선순위 큐 삽입]")
pQ.enqueue(1)
pQ.enqueue(2)
pQ.enqueue(4)          
pQ.enqueue(3)
pQ.enqueue(7)
pQ.enqueue(6)
pQ.enqueue(6)
pQ.enqueue(10)
pQ.enqueue(9)
pQ.enqueue(8)
pQ.display("[중위 순회] : ")
print("peek 진행 : ", pQ.peek().key)
pQ.dequeue()
pQ.display("[삭제 연산 후 중위 순회] : ")
print("peek 진행 : ", pQ.peek().key)
pQ.dequeue()
pQ.display("[삭제 연산 후 중위 순회] : ")