x = int(input("Nhap x: "))
n = int(input("Nhap n: "))

S = 0
for i in range(1, n+1 ):
    T = x**(2*i+1)
    M = 1
    for j in range(1, 2*i+1):
        M *= j
        S += (T/M)
print("S= ", S)