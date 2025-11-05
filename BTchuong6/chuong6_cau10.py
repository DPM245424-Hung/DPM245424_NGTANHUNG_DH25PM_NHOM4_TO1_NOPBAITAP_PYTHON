def taomatran():
    sodong = int(input("Nhập số dòng của ma trận: "))
    socot = int(input("Nhập số cột của ma trận: "))
    dong = []
    for i in range(sodong):
        cot = []
        for j in range(socot):
            v = int(input(f"Nhập phần tử tại dòng {j+1}, cột {i+1}: "))
            cot.append(v)
        dong.append(cot)
    return dong
def xuatmatran(matran):
    for dong in matran:
        for v in dong:
            print(v, end='\t')
        print()
def congmatran(A, B):
    C = []
    for i in range(len(A)):
        dong = []
        for j in range(len(A[i])):
            dong.append(A[i][j] + B[i][j])
        C.append(dong)
    return C
def matranhoanvi(matran):
    hoanvi = []
    for j in range(len(matran[0])):
        dong = []
        for i in range(len(matran)):
            dong.append(matran[i][j])
        hoanvi.append(dong)
    return hoanvi


print("Nhập ma trận A:")
A = taomatran()
xuatmatran(A)

print("Nhập ma trận B:")
B = taomatran()
xuatmatran(B)

C = congmatran(A, B)
print("Ma trận C = A + B là:")
xuatmatran(C)

D = matranhoanvi(A)
print("Ma trận chuyển vị của ma trận A là:")
xuatmatran(D)
E = matranhoanvi(B)
print("Ma trận chuyển vị của ma trận B là:")
xuatmatran(E)

