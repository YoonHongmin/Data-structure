top = [ ]
def isEmpty() :
    return len(top) == 0
def push(item) :
    top.append(item)
def pop():
    if not isEmpty():
        return top.pop(-1) # -1은 맨 뒤 항목(생략 가능)
def peek():
    if not isEmpty():
        return top[-1]
def size(): return len(top)
def clear():
    global top
    top = []
def display(t) :
    for i in range(len(t)-1, -1, -1):
        print(t[i], end=' ')

for i in range(1,6):
    push(i)
print(top)
print(pop())
print(pop())
push("안녕")
print(top)
display(top)