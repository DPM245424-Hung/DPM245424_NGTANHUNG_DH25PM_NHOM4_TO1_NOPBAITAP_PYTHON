import math

try:
    r = float(input("nhap ban kinh hinh tron: "))
    cv=r*math.pi*2
    dt=r**2
    print("chu vi = ",cv)
    print("dientich",dt)
except:
    print("loi!")
