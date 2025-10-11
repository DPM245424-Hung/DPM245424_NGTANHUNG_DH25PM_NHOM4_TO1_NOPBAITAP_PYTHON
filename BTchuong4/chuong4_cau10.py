import time
def hinh1(n):
    for i in range(1, n+1):
        print(" "+"  "*(n-1)+" *"*i)
    print("* "*(2*n+1))
    for k in range(n,0,-1):
        print("* "*k)
    print()
    
def hinh2(n):
    print(" "+"  "*(n-1)+" *")
    for i in range(1, n):
        print(" "+"  "*(n-1)+" *"+"  "*(i-1)+" *")
    print("* "*(2*n+1))
    for k in range(n-1,0,-1):
        print("*"+"  "*(k-1)+" *")
    print("*")
    print()
    
def hinh3(n):
    for i in range(n+1,1,-1):
        print("  "*(n)+" *"*i)
    print("  "*(n)+" *")
    for k in range(2,n+2):
        print("  "*(n+1-k)+" *"*k)
    print()

def hinh4(n):
    print("  "*n+" *"*(n+1))
    for i in range(n-2,-1,-1):
        print("  "*n+" *"+"  "*(i)+" *")
    print("  "*(n)+" *")
    for k in range(2, n+1):
        print("  "*(n+1-k)+" *"+"  "*(k-2)+" *")
    print(" *"*(n+1))
    print()

def main():
    n = 3
    hinh1(n) 
    time.sleep(5)
    hinh2(n)
    time.sleep(5)
    hinh3(n)
    time.sleep(5)
    hinh4(n)


main()