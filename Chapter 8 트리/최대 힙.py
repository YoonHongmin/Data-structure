class MaxHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(0) # 0번 항목은 사용하지 않음
    def size(self): return len(self.heap)-1
    def isEmpty(self): return self.size() == 0
    def Parent(self, i) : return self.heap[i//2]   # 부모노드 반환
    def Left(self, i) : return self.heap[i*2]  # 왼쪽 자식노드 반환
    def Right(self, i) : return self.heap[i*2+1]  # 오른쪽 자식노드 반환
    def display(self, msg = '힙 트리: ') : print(msg, self.heap[1:])

    def insert(self, n) :
        self.heap.append(n)
        i = self.size()
        while(i !=1 and n > self.Parent(i)):    # 부모노드보다 크다면 (자신보다 큰 부모노드를 만나기 전 까지)
            self.heap[i] = self.Parent(i)   # 부모를 끌어내림
            i = i // 2  # i를 부모의 인덱스로 올림
        self.heap[i] = n

    def delete(self) :  # 삭제연산은 root 노드부터 삭제함
        parent = 1  # root 노드부터 시작
        child = 2   # 2번노드 ( root의 왼쪽 자식 )
        if not self.isEmpty() :
            hroot = self.heap[1]    # 삭제할 노드 를 hroot에 저장 , 이때는 첫번째 노드
            last = self.heap[self.size()]
            while (child <= self.size()):
                # 왼쪽 노드가 보통 더 크지만 오른쪽 노드가 더 크다면 child를 1 증가시킴 . last, 즉 마지막 노드르 맨 위로 올림
                if child<self.size() and self.Left(parent) < self.Right(parent) : child += 1
                if last >=self.heap[child] : break; # 힙 삭제 종료조건 맨 마지막 노드가 child, 즉 자식 노드보다 크다면 종료
                self.heap[parent] = self.heap[child]   # down-heap 계속
                parent = child
                child *= 2

            self.heap[parent] = last   # 맨 마지막 노드를 parent 위치 복사
            self.heap.pop(-1)   # 맨 마지막 노드 삭제
            return hroot    # 저장한(삭제한) 루트 반환
        
heap = MaxHeap()
data =[2,5,4,8,9,3,7,3]
print("[삽입 연산]: ", data)
for elem in data:
    heap.insert(elem)
heap.display("[삽입 후] : ")
heap.delete()
heap.display("[삭제 후] : ")
heap.delete()
heap.display("[삭제 후] : ")
