from random import randrange

def makelist(n):
    mainlist=[]
    for i in range(n):
        listrandompossiblevalues=[] 
        listrandompossiblevalues.append(randrange(0,100))
        if(listrandompossiblevalues[0] not in mainlist):
            mainlist+=listrandompossiblevalues
        else:
            makelist(n-i)
    return mainlist
def main():
    n = int(input("Nhập số phần tử cho list(0->100): "))
    if n > 100:
        print("Thôi nào! Số phần tử không được lớn hơn 100")  
    list = makelist(n)
    print("List sau khi tạo ngẫu nhiên là:")
    print(list)
main()


