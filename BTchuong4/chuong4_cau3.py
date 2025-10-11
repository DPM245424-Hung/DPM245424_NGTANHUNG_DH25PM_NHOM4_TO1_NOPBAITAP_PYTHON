def BMI(KG,M):
    return KG/(M**2)
def Nhap_Tinh_Trang_Co_The():
    while True:
        kg = float(input("Nhập cân nặng (kg): "))
        m = float(input("Nhập chiều cao (m): "))
        if kg <= 0 or m <= 0 or not isinstance(kg, float) or not isinstance(m, float):
            print("Cân nặng hoặc chiều cao không hợp lệ, vui lòng nhập lại")
        else:
            break
    return kg, m
def Phan_Loai(BMI):
    Phanloai = ""
    Nguyco = ""
    if BMI < 18.5:
        Phanloai = "Gầy"
        Nguyco = "Thấp"
        return Phanloai,  Nguyco
    if 18.5 <= BMI < 24.9:
        Phanloai = "Bình thường"
        Nguyco = "Trung bình"
        return Phanloai,  Nguyco
    if 25 <= BMI < 29.9:
        Phanloai = "Hơi béo phì"
        Nguyco = "Cao"
        return Phanloai,  Nguyco
    if 30 <= BMI < 34.9:
        Phanloai = "Béo phì cấp độ 1"
        Nguyco = "cao"
        return Phanloai,  Nguyco
    if 35 <= BMI < 39.9:
        Phanloai = "Béo phì cấp độ 2"
        Nguyco = "Rất cao"
        return Phanloai,  Nguyco
    if BMI >= 40:
        Phanloai = "Béo phì cấp độ 3"
        Nguyco = "Nguy hiểm"
        return Phanloai,  Nguyco
def in_KqBMI():
    print("Phân loại dựa trên Số liệu của bạn:", kg, "kg và", m, "mét")
    print("Chỉ số BMI của bạn là: ", round(BMI(kg, m),2))
    print("Bạn thuộc loại: ", Phan_Loai(BMI(kg, m))[0])
    print("Nguy cơ mắc các bệnh: ", Phan_Loai(BMI(kg, m))[1])
def main(): 
    global kg, m
    kg, m = Nhap_Tinh_Trang_Co_The()
    in_KqBMI()
main()