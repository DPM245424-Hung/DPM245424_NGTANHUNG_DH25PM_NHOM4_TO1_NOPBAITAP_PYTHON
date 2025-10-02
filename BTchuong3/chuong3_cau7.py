
day = int(input("Nhập vào ngày: "))
Month = int(input("Nhập vào tháng: "))
Year = int(input("Nhập vào năm: "))
if Year >= 0:
    newYear = Year
    if Month >= 1 and Month <= 12:
        if Month == 2:
            if (Year % 4 == 0 and Year % 100 != 0) or Year % 400 == 0:
                if day >= 1 or day <= 29:
                    if day == 29:
                        newday = 1
                        newMonth = Month+1
                    else:
                        newday = day + 1
                        newMonth = Month
                else:
                    print("Ngày không hợp lệ")
            else:
                if day >= 1 or day <= 28:
                    if day == 28:
                        newday = 1
                        newMonth = Month + 1 
                    else:
                        newday = day + 1
                        newMonth = Month
                else:
                    print("Ngày không hợp lệ")
        elif Month in (4, 6, 9, 11):
            if day >= 1 or day <= 30:
                if day == 30:
                    newday = 1
                    newMonth = Month + 1  
                else:
                    newday = day + 1
                    newMonth = Month
            else:
                print("Ngày không hợp lệ")
        elif Month in (1, 3, 5, 7, 8, 10):
            if day >= 1 or day <= 31:
                if day == 31:
                    newday = 1
                    newMonth = Month + 1
                else:
                    newday = day + 1
                    newMonth = Month 
            else:
                print("Ngày không hợp lệ")
        elif Month == 12:
            if day >= 1 or day <= 31:
                if day == 31:
                    newday = 1
                    newMonth = 1
                    newYear = Year + 1
                else:
                    newday = day + 1
                    newMonth = Month
            else:
                print("Ngày không hợp lệ")
        print("Ngày tiếp theo là: ", newday, "/", newMonth, "/", newYear)
else:
    print("Năm không hợp lệ")