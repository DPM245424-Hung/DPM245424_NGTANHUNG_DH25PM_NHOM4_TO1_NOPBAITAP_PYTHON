from math import sqrt
def nhaplist():
    list = []
    n = int(input("Nhập số phần tử của list: "))
    for i in range(n):
        v = int(input(f"Nhập phần tử thứ {i+1}: "))
        list.append(v)
    return list
def printsole():
    sl = 0
    for i in range(len(list)):
        if list[i] % 2 != 0:
            print(list[i], end = " ")
            sl += 1
    print(f"\nSố lượng số lẻ trong list là: {sl}")

def printsochan():
    sl = 0
    for i in range(len(list)):
        if list[i] % 2 == 0:
            print(list[i], end = " ")
            sl += 1
    print(f"\nSố lượng số chẵn trong list là: {sl}")

def songuyento():
    listaf = []
    for i in range(len(list)):
        if list[i] < 2:
            continue
        for j in range(2, int(sqrt(list[i]))+1):
            if list[i] % j == 0:
                listaf.append(list[i])
                break
    print("Các số nguyên tố trong list là:")
    for k in listaf:
        list.remove(k)
    print(list)
    print("Số không phải số nguyên tố trong list là:")
    print(listaf)

global list
list = nhaplist()
print("List sau khi nhập là:")
print(list)
print("Các số lẻ trong list là:")
printsole()
print("Các số chẵn trong list là:")
printsochan()
songuyento()
