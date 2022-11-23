class Set:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    
    def display(self,msg='set의 내용물'):
        print(msg,self.items)

    def contains(self,item):
        for i in range(0,len(self.items)):
            if self.items[i] == item:
                return i
        return None
    
    def insert(self,elem):
        if not self.contains(elem):
            self.items.append(elem)

    def delete(self,elem):
        if self.contains(elem):
            self.items.remove(elem)

    def sort(self):
        n = len(self.items)
        for i in range(1,n):
            key = self.items[i]  # key는 첫번째 데이터 부터 시작
            j = i-1 # j는 key 바로 전 데이터
            while j>=0 and self.items[j] > key : # 직전 데이터가 key 데이터보다 크면
                self.items[j+1] = self.items[j]   # 앞으로 한자리씩 땡김 ( 들어갈 자리를 찾음 )
                j -= 1  
            self.items[j + 1] = key  # 들어갈 자리를 찾으면 key값을 그곳에 넣음

    def __eq__(self,setB):
        if self.size() != setB.size():
            return False
        for idx in range(len(self.items)):
            if self.items[idx] != setB.items[idx]:
                return False
        return True

    def union(self, setB):  # 이 합집합 함수는 둘다 정렬된 집합에서만 사용 가능 !!!!
        newSet = Set()  # 새로운 집합 생성
        a = 0
        b = 0
        while a < len(self.items) and b < len(setB.items):  # a,b가 0부터 1씩 증가해 둘중에 하나라도 집합의 크기만큼 도달하기 전까
            valueA = self.items[a]
            valueB = setB.items[b]
            if valueA < valueB :    # B가 A보다 크면
                newSet.items.append(valueA) # 작은 값(A) append
                a += 1  # 다음 항목으로 넘어감
            elif valueA > valueB :  # A가 B보다 크면
                newSet.items.append(valueB) # 작은값(B) append
                b += 1  # 다음 항목으로 넘어감
            else :   # A와 B가 같으면
                newSet.items.append(valueA) # A또는 B중 하나만 append하고
                a += 1  # 둘다 다음항목으로 넘어감
                b += 1
        # while문이 끝남 -> 둘중에 하나의 집합이라도 마지막까지 도달함
        while a < len(self.items):  # a가 남아있다면 끝까지 도달할 때 까지
            newSet.items.append(self.items[a])  # 남은 원소들을 다 추가해줌
            a += 1
        while b < len(self.items) : # b가 남아있다면 끝까지 도달할 때 까지
            newSet.items.append(setB.items[b])  # 남은 원소들을 다 추가해줌
            b += 1
        return newSet

    def intersect(self,setB):
        newSet = Set()  # 새로운 집합 생성
        a = 0
        b = 0
        while a < len(self.items) and b < len(setB.items):  # a,b가 0부터 1씩 증가해 둘중에 하나라도 집합의 크기만큼 도달하기 전까
            valueA = self.items[a]
            valueB = setB.items[b]
            if valueA < valueB :    # B가 A보다 크면
                a += 1  # 다음 항목으로 넘어감
            elif valueA > valueB :  # A가 B보다 크면
                b += 1  # 다음 항목으로 넘어감
            else :   # A와 B가 같으면
                newSet.items.append(valueA) # A또는 B중 하나만 append하고
                a += 1  # 둘다 다음항목으로 넘어감
                b += 1
        return newSet

    def difference(self,setB):
        newSet = Set()  # 새로운 집합 생성
        a = 0
        b = 0
        while a < len(self.items) and b < len(setB.items):  # a,b가 0부터 1씩 증가해 둘중에 하나라도 집합의 크기만큼 도달하기 전까
            valueA = self.items[a]
            valueB = setB.items[b]
            if valueA < valueB :    # B가 A보다 크면
                newSet.items.append(valueA) # 작은 값(A) append
                a += 1  # 다음 항목으로 넘어감
            elif valueA > valueB :  # A가 B보다 크면
                b += 1  # 다음 항목으로 넘어감
            else :   # A와 B가 같으면
                a += 1  # 둘다 다음항목으로 넘어감
                b += 1
        # while문이 끝남 -> 둘중에 하나의 집합이라도 마지막까지 도달함
        while a < len(self.items):  # a가 남아있다면 끝까지 도달할 때 까지
            newSet.items.append(self.items[a])  # 남은 원소들을 다 추가해줌
            a += 1
        return newSet



set1 = Set()
set2 = Set()

set1.insert(3),set1.insert(4),set1.insert(1),set1.insert(7),set1.insert(5),set1.insert(6)
set2.insert(1),set2.insert(8),set2.insert(6),set2.insert(5),set2.insert(2),set2.insert(9)

set1.display("정렬 전 set1 내용물 :")
set2.display("정렬 전 set2 내용물 :")

set1.sort()
set2.sort()

set1.display("정렬 후 set1 내용물 :")
set2.display("정렬 후 set2 내용물 :")

set3 = set1.union(set2)
set3.display("집합 1과 집합2의 합집합 : ")

set4 = set1.intersect(set2)
set4.display("집합 1과 집합2의 교집합 : ")

set5 = set1.difference(set2)
set5.display("집합 1과 집합2의 차집합 : ")