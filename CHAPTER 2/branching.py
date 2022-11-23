dan = int(input("구구단 단 입력 :"))
for i in range(2,10,1):
    print("%d x %d = " %(dan, i), dan*i)
print("%d x %d = "%(2 , 1), "그리고 : %d "%dan)