class Stack :
    def __init__(self):
        self.top = []
    def isEmpty(self): 
        return len(self.top) == 0
    def size(self):
        return len(self.top)
    def clear(self):self.top=[]
    def push(self,item):
        self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop()
    def peek(self): 
        if not self.isEmpty():
            return self.top[-1]

    def __str__(self):return str(self.top)

def precedence (op):    # 연산자 우선순위 함수, 숫자가 높을수록 우선순위 높음
    if op == '(' or op == ')': return 0     
    elif op == '+' or op == '-': return 1
    elif op == '*' or op == '/': return 2      
    else : return -1

def Infix2Postfix(expr) :
    s = Stack()
    output = []
    for term in expr :
        if term in '(' :
            s.push(term)
        elif term in ')' :
            while not s.isEmpty():
                op = s.pop()
                if op == '(': break;
                else : 
                    output.append(op)
        elif term in "+-*/":    # 연산자이면
            while not s.isEmpty():
                op = s.peek()
                if( precedence(term)<=precedence(op)):  # ArrayStack의 top 연산자(op)와 term 우선순위 비교 
                    output.append(op)   #  top 연산자 우선순위가 높으면 top 연산자 pop()후 term push()
                    s.pop()
                else : break    # top 연산자 우선순위가 term 연산자 보다 낮다면 그 위에 term push()
            s.push(term)
        else : 
            output.append(term)

    while not s.isEmpty(): 
        output.append(s.pop())
    return output

expr1 = ['8','/','2','-','3','+','(','3','*','2',')']
print(Infix2Postfix(expr1))