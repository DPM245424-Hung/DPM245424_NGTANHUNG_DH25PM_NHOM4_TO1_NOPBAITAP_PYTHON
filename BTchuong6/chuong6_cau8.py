list = []
n = int(input("Nhập số phần tử của list: "))
for i in range(n):
    v = int(input(f"Nhập phần tử thứ {i+1}: "))
    list.append(v)
print("List sau khi sắp xếp giảm dần là:")
for i in range(n):  
    for j in range(i+1,n):
        if list[i] < list[j]:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
print(list)