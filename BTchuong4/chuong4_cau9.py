from math import sqrt

def nhap_lan_long():
    while True:
        try:
            n = int(input("Nhập số lần lồng nhau: "))
            if n > 0:
                return n
            else:
                print("Vui lòng nhập số nguyên dương.")
        except ValueError:
            print("không hợp lệ. Vui lòng nhập lại.")

def Tinh(n):
    S = 0
    for i in range(n):
        S = sqrt(2 + S)
    return S
def main():
    n = nhap_lan_long()
    print("Kq là:", Tinh(n))
    print("Kq là:",  sqrt(2 + sqrt(2 + sqrt(2)))) # check khi n = 3

main()