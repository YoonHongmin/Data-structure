class Entry:
    def __init__( self, key, value ):
        self.key = key
        self.value = value

    def __str__(self):
        return str("%s:%s"%(self.key, self.value))

class LinearProMap:
    def __init__( self, M ):
        self.table = [None]*M
        self.data = [None]*M  #key관련 데이터
        self.M = M

    def hashFn(self,key):
        sum = 0
        for c in key :
            sum = sum + ord(c)
        return sum % self.M
    
    def insert(self,key,value):
        idx = self.hashFn(key)
        i = idx
        j = 0
        while True: #삽입할 위치 조건
            if self.table[i] == None or self.table[i] == ' ': #공백 혹은 None인 경우
                self.table[i] = key #key를 해시 테이블에 저장
                self.data[i] = value #key 관련 데이터 저장
                return
            if self.table[i] == key: #이미 key가 존재하면
                self.data[i] = value #데이터만 저장
                return
            j += 1
            i = (idx + j)%self.M #i의 다음위치 계산
            if i == idx: # i가 초기위치와 같으면 루프
                break

    def search(self,key): #탐색 연산
        idx = self.hashFn(key) #초기 해시 주소 계산
        i = idx
        j = 1
        while self.table[i] != None: #a[i]가 공백이 아닐 시
            if self.table[i] == key: #탐색 성공
                return self.data[i] #탐색한 key 데이터 반환
            j += 1
            i = (idx + j)%self.M #다음 위치로
            if i == idx: #i가 초기위치와 같으면 종료
                return None #탐색 실패
        return None #탐색 실패
    
    def delete(self,key):
        idx = self.hashFn(key)
        i = idx
        j = 1
        while self.table[i] != None: #a[i]가 공백이 아니면
            if self.table[i] == key: #삭제할 테이블의 키에 대해
                self.table[i] = ' ' #key 값은 없애고
                self.table[i] = None #그 데이터는 None으로
            j += 1
            i = (idx+j)%self.M #다음위치로
            if i == idx: #초기위치로 돌아오면 종료
                return None #삭제 실패
        return None #삭제 실패

    def display(self, msg): #맵 출력 함수
        print(msg) #메시지 출력
        for idx in range(len(self.table)): #맵 전체 탐색
            entry = self.table[idx] #탐색 후 각 위치의 해당 키
            print("[%2d] -> "%idx, self.table[idx]) #메시지 출력 

map = LinearProMap(13)
map.insert('hongmin', '윤홍민')
map.insert('hojin', '박호진')
map.insert('onehunseop', '원현섭')
map.insert('koreatech', '한기대')
map.insert('computer', '컴퓨터')
map.display("나의 단어장 : ")

print(" 탐색:game ==> ", map.search('hongmin'))
print(" 탐색:over ==> ", map.search('structure'))
print(" 탐색:data ==> ", map.search('koreatech'))

map.delete('hojin')
map.display("나의 단어장: ")
print(" 탐색:hojin --> ", map.search('hojin'))