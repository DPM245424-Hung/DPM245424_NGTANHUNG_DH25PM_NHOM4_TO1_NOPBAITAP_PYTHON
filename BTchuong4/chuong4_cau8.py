import math
def nhap_so():
    while True:
        try:
            a = int(input("Nhập a: "))
            x = int(input("Nhập x: "))
            if a > 0 and x > 0:
                return a, x
            else:
                print("Vui lòng nhập số nguyên dương.")
        except ValueError:
            print("không hợp lệ. Vui lòng nhập lại.")

def log(a, x):
    if a == 1:
        print("không xác định do a = 1")
    else:
        print(f"log(a)X =", math.log(x, a))

def main():
    a, x = nhap_so()
    log(a, x)


main()