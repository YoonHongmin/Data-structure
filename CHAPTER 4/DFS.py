map = [ ['1','1','1','1','1','1'],
        ['e','0','0','0','0','1'],
        ['1','0','1','0','1','1'],
        ['1','1','1','0','0','x'],
        ['1','1','1','0','1','1'],
        ['1','1','1','1','1','1']]
MAX_SIZE = 6
class Stack :
    def __init__(self):self.top = []
    def isEmpty(self):return self.size == 0
    def size(self):return len(self.top)
    def clear(self):self.top=[]
    def push(self,item):self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop()
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
    def __str__(self):
        return str(self.top[::-1])  # 가장 늦게 들어간게 가장 나중에 출력되도록 함. 왼쪽이 스택 입구

def isValidPos(x,y):
    if x<0 or y<0 or x>=MAX_SIZE or y>=MAX_SIZE :
        return False
    else :
        return map[y][x] =='0' or map[y][x] =='x'
def DFS():
    stack = Stack()
    stack.push((0,1))
    print('DFS: ')

    while not stack.isEmpty():
        here = stack.pop()
        (x,y) = here
        print(here, end='==>')
        if map[y][x] == 'x' :
            print("남은 스택 : ", stack) 
            return True
        else :
            map[y][x] ='.'
            if isValidPos(x,y-1):stack.push((x,y-1))
            if isValidPos(x,y+1):stack.push((x,y+1))
            if isValidPos(x-1,y):stack.push((x-1,y))
            if isValidPos(x+1,y):stack.push((x+1,y))
        print('현재 스택 : ', stack)
    return False
result = DFS()
if result : print('--> 미로탐색 성공')
else : print('--> 미로탐색 실패')