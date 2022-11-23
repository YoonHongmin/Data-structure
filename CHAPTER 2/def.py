def find_max(a) :
    max = a[0]
    min = a[0]
    for i in range(len(a)):
        if max < a[i] :
            max = a[i]
        if min > a[i] :
            min = a[i]
    return (max, min)   # 튜플

def sum_range(start,end,step=1) :
    sum = 0
    for i in range(start,end,step) :
        sum = sum + i
    return sum

arr = [ 5, 2, 3, 6, 10, 2, 12, 4]
(x,y)= find_max(arr)    # 튜플
print("가장 큰 숫자와 작은 숫자는 :",(x,y)) # 튜플
print(sum_range(1,10))
print(sum_range(end = 10, start = 1))