try:
    toan = float(input("nhap diem toan: "))
    hoa = float(input("nhap diem hoa: "))
    ly = float(input("nhap diem ly: "))
    DiemTB = (toan+ly+hoa)/3
    print("diem trung binh ca ba mon = ",DiemTB)
    print("diem trung binh duoc lam tron = ",round(DiemTB,2))
except:
    print("loi!")