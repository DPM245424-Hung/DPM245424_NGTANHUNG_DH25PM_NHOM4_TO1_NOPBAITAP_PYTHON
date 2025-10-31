def CheckDoiXung(s):
    check = False
    for i in range(len(s)):
        if s[i]==s[len(s)-i-1]:
            check = True
            break
    return check

def main():
    print("Nhập 1 chuỗi số bất kì:")
    s=input()
    if(CheckDoiXung(s)):
        print("Chuỗi bạn nhập đối xứng")
    else:
        print("Chuỗi bạn nhập không đối xứng")

while True:
    main()
    print("Tiếp tục với 1 chuỗi khác không?(c/k):")
    s=input()
    if s=='k' or s=='K':
        break
    print("CÁM ƠN BẠN ĐÃ SỬ DỤNG!")