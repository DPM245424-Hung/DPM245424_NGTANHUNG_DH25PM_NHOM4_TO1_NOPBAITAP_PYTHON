def NegativeNumberInStrings(str):
    a = str
    for i in range (len(a)):
        if a[i] == '-':
            if i+1 < len(a) and a[i+1].isdigit(): # check sau dau '-'la so
                j = i + 2
                while j < len(a) and a[j].isdigit(): #so lien tiep
                    j += 1
                yield int(a[i:j]) #tra ve gia tri cho n ngoai ham
                i = j
            else:
                i += 1
        else:
            i += 1
def main():
    s = input("Nhập chuỗi ký tự: ")
    print("Chuỗi ban đầu:", s)
    print("Các số âm trong chuỗi là:")

    for n in NegativeNumberInStrings(s):
        print(n)
    
main()