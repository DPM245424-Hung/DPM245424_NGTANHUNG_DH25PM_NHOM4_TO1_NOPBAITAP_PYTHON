n = int(input(":Nhap n: "))
print("box")
print("* " * n)
for i in range(n - 2):
    print("* " + "  " * (n - 2) + "*")
print("* " * n)

print("triangle")
for i in range(n):
        print("  "* (n - i) + "* "* (i))

print("2 triangles combined at resverse position")
m = n-1
print("* ")
for i in range(m):
    print("*" + "  "*(m - (m - i)) + " *")
print("* " * ((2*n)+1))
for i in range(m):
    print("  "*(2*m - (m-i)+2)+ "*"+"  "* (m-i-1)+ " *")
print("  "* (2*n) +"*")
