def ROI(DT,CP):
    return (DT - CP) / CP
def Nhap_Loi_Nhuan():
    while True:
        dt = float(input("Nhập doanh thu: "))
        cp = float(input("Nhập chi phí: "))
        if dt <= 0 or cp <= 0 or not isinstance(dt, float) or not isinstance(cp, float):
            print("Doanh thu hoặc chi phí không hợp lệ, vui lòng nhập lại")
        else:
            break
    return dt, cp
def Quyet_dinh(ROI):
    if ROI < 0.75:
        print("Không nên đầu tư!")
    else:
        print("Nên đầu tư!")
def main():
    dt, cp = Nhap_Loi_Nhuan()
    print("Lợi nhuận của bạn là: ", round(ROI(dt, cp)*100,2), "%")
    print("Dựa trên lợi nhuận của bạn, chúng tôi khuyên bạn:")
    Quyet_dinh(ROI(dt, cp))

main()