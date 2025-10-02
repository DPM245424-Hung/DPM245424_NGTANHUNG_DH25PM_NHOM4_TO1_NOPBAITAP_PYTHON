a = 0
while a<100:
    b = 0
    while b<40:
        if(a+b)%2==0:
            print("*",end="")
        b+=1
    print()
    a+=1

'''
a tượng trưng cho số dòng, b tượng trưng cho số cột => 40 cột, 100 dòng => 4000 dấu *
'''