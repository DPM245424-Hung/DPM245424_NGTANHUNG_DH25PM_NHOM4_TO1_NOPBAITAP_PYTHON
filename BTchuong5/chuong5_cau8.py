def laynamemp3(str):
    for i in range(len(str),0,-1):
        if str[i-4:i].lower() == '.mp3':
            j = i - 5
            while str[j].isalnum() or str[j] in ('_', '-'):
                j -= 1
            yield str[j+1:i]
def layname(str):
    for i in range(len(str),0,-1):
        if str[i-4:i].lower() == '.mp3':
            j = i - 5
            while str[j].isalnum() or str[j] in ('_', '-'):
                j -= 1
            yield str[j+1:i-4]
                
def main():
    s = input("Nhập chuỗi ký tự: ")
    print("Chuỗi ban đầu:", s)
    print("Các tên file mp3 trong chuỗi là:")

    for n in laynamemp3(s):
        print(n)
    print("Các tên file (không có đuôi .mp3) trong chuỗi là:")
    for m in layname(s):
        print(m)
main()