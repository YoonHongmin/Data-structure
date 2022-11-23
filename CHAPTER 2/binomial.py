def binomial(n,k):
    if k == 0 or k == n :
        return 1
    return binomial(n-1,k-1) + binomial(n-1,k)

def binomial_iter(n,k) :
    top = 1
    bottom = 1
    for i in range(n,n-k,-1) :
        top = top * i
    for i in range(1,k+1):
        bottom = bottom * i
    return float(top/bottom)

m = binomial(2,1)
print(m)
l = binomial_iter(2,1)
print(l)