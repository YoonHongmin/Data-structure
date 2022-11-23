def sum_range(n,k):
    if k == 0 or k == n : return 1
    return sum_range(n-1,k-1) + sum_range(n-1,k)

print(sum_range(100,3)) 