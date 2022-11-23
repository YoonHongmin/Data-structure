
from tempfile import tempdir


def nCr(n,r):
    if r == 0 or r == n:
        return 1
    return nCr(n-1,r) + nCr(n-1,r-1)

def nCr_iter(n,r):
    sum = 1
    for i in range (r):
        sum *= n
        n -= 1
    for i in range(1,r+1):
        sum /= i
    return int(sum)

def sum_range(n) :
    if n == 1 : return 1
    return 1/n + sum_range(n-1)

def sum_range_iter(n):
    sum = 0
    for i in range(1,n+1):
        sum += 1/i
    return sum

def power(x,n):
    if n == 0 : return 1
    if n%2 == 0:
        return power(x*x, n//2)
    else :
        return x*power(x*x, (n-1)//2)    

def power_iter(x,n):
    sum = 1
    for i in range(n):
        sum *= x
    return sum

def factorial(n):
    if n == 1 : return 1
    return n * factorial(n-1)

def factorial_iter(n):
    sum = 1
    for i in range(1,n+1):
        sum *= i
    return sum

def fibo(n) :
    if n == 0 : return 0
    elif n == 1 : return 1
    return fibo(n-1) + fibo(n-2)

def fibo_iter(n):
    if n < 2 : return n
    last = 0
    current = 1
    for i in range(2,n+1):
        tmp = current
        current  += last
        last = tmp 
    return current

def gugu(n) :
    if n is not 0 :
        print("2 x %d = %d"%(n, 2*n))
        gugu(n-1)

print(nCr(8,3))
print(nCr_iter(8,3))

print(sum_range(5))
print(sum_range_iter(5))

print(power(2,10))
print(power_iter(2,10))


print(factorial(5))
print(factorial_iter(5))

print(fibo(10))
print(fibo_iter(10))

gugu(9)