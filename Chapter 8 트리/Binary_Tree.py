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
"""
d = TNode('D',None, None)
e = TNode('E',None, None)
b = TNode('B',d, e)
f = TNode('F',None, None)
c = TNode('C',f, None)
root = TNode('A', b ,c)
"""

h = TNode( 1 ,None ,None )  
i = TNode( 2 ,None ,None )
d = TNode( '*' , h, i)
j = TNode( 4, None ,None )
k = TNode( 2 ,None ,None )
e = TNode( '-' , j, k)
l = TNode( 1 ,None ,None )
m = TNode( 3 ,None ,None )
f = TNode( '+' , l, m)
g = TNode( 2 , None, None)
b = TNode( '+' , d, e)
c = TNode( '/' , f, g)
root = TNode('+', b, c)

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