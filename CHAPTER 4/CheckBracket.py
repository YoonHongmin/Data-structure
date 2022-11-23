# 조건 1: 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 한다.
    # 조건문을 다 돌았는데 stack에 남은 괄호가 있으면 False
# 조건 2: 같은 타입의 괄호에서 왼쪽 괄호가 오른쪽 괄호보다 먼저 나와야 한다.    
    # 스택이 비어있을 때 오른쪽 괄호(닫히는 괄호)가 나오면 False
# 조건 3: 서로 같은 타입의 괄호 쌍이 서로를 교차하면 안 된다.
    # 닫히는 괄호가 나오면, stack에서 pop 하는데 쌍이 다르면 False
# 열리는 괄호면 push, 닫히는 괄호면 pop을 하는데 pop한 괄호와 일치해야한다.
class Stack :
    def __init__(self):self.top = []
    def isEmpty(self): return len(self.top) == 0
    def size(self):return len(self.top)
    def clear(self):self.top=[]
    def push(self,item):self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
    def __str__(self):return str(self.top)

def checkBrackets(statement):
    stack = Stack()
    for ch in statement:
        if ch in ('(','[','{'):
            stack.push(ch)
        elif ch in (')',']','}'):
            if stack.isEmpty():
                return False    # 조건 2 위반
            else :
                left = stack.pop()
                if (ch ==")" and left !="(") or (ch =="]" and left !="[") or (ch =="}" and left !="{"):
                    return False    # 조건 3 위반
    return stack.isEmpty()

str = ("(([{)", "init__(self)","[(stack).isEmpty]" )
for s in str:
    m = checkBrackets(s)
    print(s,"-->",m)