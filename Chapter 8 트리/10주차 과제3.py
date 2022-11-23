MAX_QSIZE = 10

class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

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
    
def preorder(n) :
    if n is not None :
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)
def inorder(n) :
    if n is not None :
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)
def postorder(n) :
    if n is not None :
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')
def levelorder(root) :
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty() :
        n = queue.dequeue()
        if n is not None :
            print(n.data, end =' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)
def count_node(n):
    if n is None :
        return 0
    else :
        return 1 + count_node(n.left) + count_node(n.right)
def count_leaf(n) :
    if n is None :
        return 0
    elif n.left is None and n.right is None :
        return 1
    else :
        return count_leaf(n.left) + count_leaf(n.right)
def calc_height(n):
    if n is None :
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight) :
        return hLeft + 1
    else :
        return hRight + 1

def isLeaf(n) :
    if n.left is None and n.right is None : return True
    else : return False  

def isFullNode(n) :
    if n.left is not None and n.right is not None : return True;
    else : return False


def is_complete_binary_tree(root):
    if root is None : return True;

    q = CircularQueue()
    q.enqueue(root)

    while(q.size() is not 0) :
        temp = q.peek()
        if isFullNode(temp) is not True :
            if temp.left is None and temp.right is not None : return False
            else :
                if temp.left is not None :
                    q.enqueue(temp.left)
                q.dequeue()
                break
        else :
            q.enqueue(temp.left)
            q.enqueue(temp.right)
            q.dequeue()

    while (q.size() is not 0) :
        temp = q.peek()
        if isLeaf(temp) is not True : return False
        else : q.dequeue()
    
    return True

def level(root,node,lev=1): 
   if root==None : return 0 
   if root==node : return lev 
   if root.left==None and root.right==None : return 0

   tright = level(root.right,node,lev+1) 
   tleft = level(root.left,node,lev+1) 
   if tleft is 0 : return tright 
   else : return tleft  

G = TNode(3,None,None)
F = TNode(4,None,None)
C = TNode(7,F,G)
E = TNode(5,None,None)
D = TNode(6, None, None)
B = TNode(8, D,E)
root = TNode(10, B, C)

print('\n 중위표기 : ', end = '')
inorder(root)
print('\n 전위표기 : ', end = '')
preorder(root)
print('\n 후위표기 : ', end = '')
postorder(root)
print('\n Level-Order : ', end = '')
levelorder(root)
print()

print(" 노드의 개수 = %d개"% count_node(root))
print(" 단말의 개수 = %d개"% count_leaf(root))
print(" 트리의 높이 = %d"% calc_height(root))

print("완전 이진트리 검사 :", is_complete_binary_tree(root))
print("노드 A의 레벨 :", level(root, root))