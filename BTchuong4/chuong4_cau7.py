import math
def nhap_ToaDo():
    while True:
        try:
            x = float(input("Nhập hoành độ x: "))
            y = float(input("Nhập tung độ y: "))
            return (x, y)
        except ValueError:
            print("Đầu vào không hợp lệ. Vui lòng nhập lại.")
def DoDai_AB(A, B):
    return math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)
def main():
    print("Nhập tọa độ điểm A:")
    A = nhap_ToaDo()
    print("Nhập tọa độ điểm B:")
    B = nhap_ToaDo()
    DoDai = DoDai_AB(A, B)
    print(f"Độ dài đoạn thẳng AB là:", DoDai)

main()
    