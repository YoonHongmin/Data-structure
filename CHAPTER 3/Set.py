class Set:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    
    def display(self,msg='set의 내용물'):
        print(msg,self.items)

    def contains(self,item):
        return item in self.items
    
    def insert(self,elem):
        if not self.contains(elem):
            self.items.append(elem)

    def delete(self,elem):
        if self.contains(elem):
            self.items.remove(elem)
            
    def union(self,setB):
        setC = Set() # union할 set
        setC.items = list(self.items) # 깊은복사
        for elem in setB.items :
            if elem not in self.items:
                setC.items.append(elem)
        return setC
    def subset(self,setB):
        num = len(self.items)
        count = 0
        for i in range(len(setB.items)):
            if self.contains(setB.items[i]):
                count +=1
        return num == count

setA = Set()
setA.insert('빗')
setA.insert('파이썬')
setA.insert('자료구조')
setA.insert('축구공')
setA.insert('휴대폰')

setB = Set()
setB.insert('빗')
setB.insert('파이썬')
setB.insert('자료구조')
setB.insert('축구공')

setA.display()
setB.display()
print(setB.subset(setA))