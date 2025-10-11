import random
def Nhap_so():
    while True:
        n = int (input("Nhập số bạn đoán (1-100): "))
        
        if n < 0 or n > 100 or not isinstance(n, int):
            print("Số hoặc kí tự bạn nhập không hợp lệ, vui lòng nhập lại")
        else:
            break
    return n
def choi_game():
    So = random.randint(1, 100) 
    luocdoan = 0
    tiep = "c"
    while tiep == "c":
        while True:
            n = Nhap_so()
            if n != So:
                luocdoan += 1
                if luocdoan == 7:
                    print("Bạn đã thua cuộc, số đúng là", So)
                    break
                print("Rất tiếc bạn đã đoán sai! đoán lại lần: "+ str(luocdoan))
            else:
                print("Chúc mừng bạn đã đoán đúng số", So)
                break
        tiep = input("Bạn có muốn tiếp tục chơi không? (c/k): ")
        if tiep == "c" or tiep == "C":
            So = random.randint(1, 100)
            luocdoan = 0
            print("New game+!")
        else:
            print("Kết thúc trò chơi")
            break
def main():
    print("Chào mừng bạn đến với trò chơi đoán số! hãy bắt đầu nào!")
    choi_game()
    print("Cảm ơn bạn đã chơi trò chơi này, hẹn gặp lại!")
main()