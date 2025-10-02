month = int(input("Nhập vào tháng: "))
if month < 1 or month > 12:
    print("Tháng không hợp lệ")
else:
    if month in (1,2,3):
        print("Quý 1")
    elif month in (4,5,6):
        print("Quý 2")
    elif month in (7,8,9):
        print("Quý 3")
    else:
        print("Quý 4") 