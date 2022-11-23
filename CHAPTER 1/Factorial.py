def factorial(n) :  # 시간복잡도 O(n) 
    if n == 1 : return 1
    else : return n * factorial(n-1)

def factorial2(n) :  # 시간복잡도 O(n)
    sum = 1
    for i in range(n,0,-1) :
        sum = sum * i
    return sum
print(factorial(5))
print(factorial2(5))

