def nhap_so():
    while True:
        try:
            n = int(input("Nhập số nguyên dương n: "))
            if n > 0:
                return n
            else:
                print("Vui lòng nhập số nguyên dương.")
        except ValueError:
            print("không hợp lệ. Vui lòng nhập lại.")
def fibonacci(n):
    if n <=2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def list_fibonacci(n):
    for i in range(1, n+1):
        print(fibonacci(i), end=' ')
def main():
    n = nhap_so()
    print("fibonacci =", fibonacci(n))
    print(f"Các số Fibonacci đầu tiên đến số thứ {n} là:")
    list_fibonacci(n)

main()
