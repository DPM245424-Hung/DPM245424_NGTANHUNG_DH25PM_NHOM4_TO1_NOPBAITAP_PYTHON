def toiuuchuoi(str):
    m = ''
    i = 0
    h = ''
    while i < len(str):
        if str[i] != ' ':
            m += str[i]
            i += 1
        else:
            m += ' '
            while i < len(str) and str[i] == ' ':
                i += 1
    for x in range(len(m)):
        if x == 0 or m[x-1] == ' ':
            r = m[x].upper()
        else:
            r = m[x].lower()
        h += r
    return h.strip()


def main():
    s = input("Nhập chuỗi ký tự: ")
    print("Chuỗi ban đầu:", s)
    print("Chuỗi sau khi tối ưu hóa:", toiuuchuoi(s))

main()