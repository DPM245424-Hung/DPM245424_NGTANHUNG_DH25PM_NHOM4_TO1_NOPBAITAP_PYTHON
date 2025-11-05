def main():
    mainlist = []
    fisrt = int(input("Nhập phần tử đầu tiên của list: "))
    mainlist.append(fisrt)
    while True:
        n = int(input("Nhập số lần thêm phần tử vào list: "))
        print("lưu ý: các phần tử sau phải lớn hơn phần tử trước đó")
        for i in range(n):
            dem = 0
            while True:
                if dem == n:
                    break
                v =int(input(f"Nhập phần tử tiếp theo: "))
                if v > mainlist[i-1]:
                    mainlist.append(v)
                    dem += 1
                    break
        print("Bạn có muốn nhập thêm không? (y/n): ")
        lc = input().lower()
        if lc == 'n':
            break
    print("List sau khi tạo là:")
    print(mainlist)
main()