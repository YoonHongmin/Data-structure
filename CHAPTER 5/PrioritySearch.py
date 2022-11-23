
map = [ ['1','1','1','1','1','1'],
        ['e','0','0','0','0','1'],
        ['1','0','1','0','1','1'],
        ['1','1','1','0','0','x'],
        ['1','1','1','0','1','1'],
        ['1','1','1','1','1','1']]
MAX_SIZE = 6
(ox,oy) = (5,4)
def dist(x,y):
    (dx,dy) = (ox-x,oy-y)
    return sqrt(dx*dx + dy*dy)

def isValidPos(x,y):
    if x<0 or y<0 or x>=MAX_SIZE or y>=MAX_SIZE :
        return False
    else :
        return map[y][x] =='0' or map[y][x] =='x'

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
                if self.items[i][2] > self.items[highest][2]:
                    highest = i
            return highest

def isValidPos(x,y):
    if x<0 or y<0 or x>=MAX_SIZE or y>=MAX_SIZE :
        return False
    else :
        return map[y][x] =='0' or map[y][x] =='x'
def MySmartSearch():
    q = PriorityQueue()
    q.enqueue((0,1,-dist(0,1)))
    print('SmartSearch: ')

    while not q.isEmpty():
        here = q.dequeue()
        x,y,_d = here
        print(here, end='==>')
        if map[y][x] == 'x' : return True
        else :
            map[y][x] ='.'
            if isValidPos(x,y-1):q.push((x,y-1))
            if isValidPos(x,y+1):q.push((x,y+1))
            if isValidPos(x-1,y):q.push((x-1,y))
            if isValidPos(x+1,y):q.push((x+1,y))
        print('현재 스택 : ', q)
    return False

