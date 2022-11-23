class Entry:
    def __init__(self,key,value): #생성자 함수
        self.key = key #key 
        self.value = value #key 데이터

    def __str__(self):#연산자 중복함수
        return str ("%s:%s"%(self.key, self.value)) #key와 key의 데이터의 문자 반환

class LinearProbMap:
    def __init__(self, M): #생성자
        self.table = [None]*M  #해시 테이블, 크기 M
        self.data = [None]*M  #key관련 데이터
        self.M = M #해시 테이블 크기

    def hashFn(self, key): #해시 함수
        sum = 0 
        for c in key: #문자열의 모든 문자에 대해
            sum = sum + ord(c)  #하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환
        return sum % self.M #해시 주소

    def insert(self,key,value): #(key,value)입력
        idx = self.hashFn(key) #초기 해시 주소 계산
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
       
    def delete(self,key): #삭제 연산
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
#----------------------------------------------------------테스트 프로그램---------------------------------------------------------------
map = LinearProbMap(13)
map.insert('data', '자료')
map.insert('structure', '구조')
map.insert('sequentail search', '선형 탐색')
map.insert('game', '게임')
map.insert('binary search', '이진탐색')
map.display("나의 단어장: ")

print("탐색:game --> ", map.search('game'))
print("탐색:over --> ", map.search('over'))
print("탐색:data --> ", map.search('data'))
print("탐색:binary search --> ", map.search('binary search'))
print("삭제:game --> ", map.search('game'))

map.delete('game')
map.display("나의 단어장: ")