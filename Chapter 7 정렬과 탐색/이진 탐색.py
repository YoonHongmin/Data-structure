
def binary_search(A, key, low, high):
    if (low <= high) :
        middle = (low + high) // 2
        if key == A[middle].key :
            return middle
        elif (key < A[middle].key) :
            return binary_search(A,key,low,middle-1)
        else :
            return binary_search(A,key,middle + 1, high)
    return None     # 탐색 실패

list = [3,5,7,10,13,14,15,16,20,22,25,27,20]
binary_search(list, 20, 0, 12)