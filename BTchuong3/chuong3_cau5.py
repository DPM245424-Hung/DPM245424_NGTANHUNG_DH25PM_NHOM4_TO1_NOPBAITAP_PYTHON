# 1. 
i =3 ,j =5 ,k =7
if i < j:
    if i < k:
        i = j
    else:
        j = k
else:
    if j > k:
        j = i
    else:
        i = k
print("i=",i,"j=",j,"k=",k)
'''
1. i,j,k = 3, 5, 7 => i=7, j=5, k=7
2. i,j,k = 3, 7, 5 => i=5, j=7, k=5
3. i,j,k = 5, 3, 7 => i=7, j=3, k=7
4. i,j,k = 5, 7, 3 => i=3, j=7, k=3
5. i,j,k = 7, 3, 5 => i=5, j=3, k=5
6. i,j,k = 7, 5, 3 => i=3, j=5,k=3
'''