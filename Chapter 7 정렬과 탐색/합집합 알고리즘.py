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

    def union(self, setB):  # 이 합집합 함수는 둘다 정렬된 집합에서만 사용 가능 !!!!
        newSet = Set()  # 새로운 집합 생성
        a = 0
        b = 0
        while a < len(self.items) and b < len(setB.items):  # a,b가 0부터 1씩 증가해 둘중에 하나라도 집합의 크기만큼 도달하기 전까
            valueA = self.items[a]
            valueB = self.items[b]
            if valueA < valueB :    # B가 A보다 크면
                newSet.items.append(valueA) # 작은 값(A) append
                newSet.display()
                a += 1  # 다음 항목으로 넘어감
            elif valueA > valueB :  # A가 B보다 크면
                newSet.items.append(valueB) # 작은값(B) append
                newSet.display()
                b += 1  # 다음 항목으로 넘어감
            else :   # A와 B가 같으면
                newSet.items.append(valueA) # A또는 B중 하나만 append하고
                a += 1  # 둘다 다음항목으로 넘어감
                b += 1
                newSet.display()
        # while문이 끝남 -> 둘중에 하나의 집합이라도 마지막까지 도달함
        while a < len(self.items):  # a가 남아있다면 끝까지 도달할 때 까지
            newSet.items.append(self.items[a])  # 남은 원소들을 다 추가해줌
            a += 1
        while b < len(self.items) : # b가 남아있다면 끝까지 도달할 때 까지
            newSet.items.append(self.items[b])  # 남은 원소들을 다 추가해줌
            b += 1
        return newSet

set1 = Set()
set2 = Set()

for i in range(1,10):
    set1.insert(i)
for i in range(3,13):
    set2.insert(i)

set1.display()
set2.display()

set3 = set1.union(set2)
set3.display("집합 1과 집합2의 합집합 : ")
    
