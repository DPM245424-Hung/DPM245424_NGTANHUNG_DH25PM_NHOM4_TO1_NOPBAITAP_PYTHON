def nhap():
    while True:
        try:
            n = int(input("nhâp 1 số nguyên dương bất kì: "))
            if n > 0:
                return n
            else:
                print("Vui lòng nhập số nguyên dương.")
        except ValueError:
            print("không hợp lệ. Vui lòng nhập lại.")

def KTSo_HoanThien(n):
    S = 0 
    for i in range(1,n):
        if n % i == 0:
            S+=i
    if S==n:
        print("Đây là số hoàn thiện! ")
    else:
        print("Đây không là số hoàn thiện! ")

def KTSo_ThinhVuong(n):
    S = 0 
    for i in range(1,n):
        if n % i == 0:
            S+=i
    if S > n:
        print("Đây là số Thịnh Vượng! ")
    else:
        print("Đây không là số Thịnh Vượng! ")

def main():
    print("<>:Kiểm tra số Hoàn thiện/Thịnh Vượng")
    n = nhap()
    KTSo_HoanThien(n)
    KTSo_ThinhVuong(n)
    L = str(input("tiếp tục với số khác? (y): "))
    if L == 'y' or L == 'Y':
        main()
main()
    