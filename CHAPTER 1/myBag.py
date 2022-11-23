import time
def contains(bag, e) : return e in bag      # 파이썬의 in 연산자 사용
def insert(bag, e) : bag.append(e)      # 파이썬 리스트의 append메소드 사용
def remove(bag, e) : bag.remove(e)      # 파이썬 리스트의 remove메소드 사용
def count(bag) : return len(bag)      # 파이썬의 len함수 사용

myBag = []
start = time.time()     # 실행시간 측정 시작
insert(myBag, '휴대폰')
insert(myBag, '빗')
insert(myBag, '손수건')
insert(myBag, '지갑')
insert(myBag, '야구공')
print('가방속의 물건', myBag)
remove(myBag, '손수건')
print('가방속의 물건', myBag)
end = time.time()       # 실행시간 측정 종료
print('실행시간', end-start)