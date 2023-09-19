a = int(input())
if a%2 == 0:
    print(int(2*(3**(a/2))))
else:
    print(int(3**(a//2)+a**((a+1)//2)))
