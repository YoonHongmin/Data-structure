
def selection_sort(A):  # 선택 정렬
    n = len(A)  # n은 리스트의 길이
    for i in range(n-1):
        least = i   # i번째 항목
        for j in range(i+1, n):
            if (A[j]<A[least]): # i번째 항목이 j번째 항목(j는 i+1부터 시작)보다 크면 
                least = j   # least에 j번째 항목을 저장 
        A[i], A[least] = A[least], A[i] # 튜플을 이용해 i번째와 j번째 값을 바꿔줌 (tmp 이용 안해도 됨)

def insertion_sort(A):  # 삽입 정렬
    n = len(A)
    for i in range(1,n):
        key = A[i]  # key는 첫번째 데이터 부터 시작
        j = i-1 # j는 key 바로 전 데이터
        while j>=0 and A[j] > key : # 직전 데이터가 key 데이터보다 크면
            A[j+1] = A[j]   # 앞으로 한자리씩 땡김 ( 들어갈 자리를 찾음 )
            j -= 1  
        A[j + 1] = key  # 들어갈 자리를 찾으면 key값을 그곳에 넣음


list1 = [10,30,50,20,40]
list2 = [5,3,8,1,4,7]
print("리스트 1번:", list1)
print("리스트 2번:", list2)

selection_sort(list1)
insertion_sort(list2)

print("리스트 1번 선택정렬 진행:", list1)
print("리스트 2번 삽입정렬 진행:", list2)