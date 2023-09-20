a = int(input())
if a%2 == 0:
    print(int((2*(3**(a/2)))%(10**9+7)))
else:
    print(int((3**(a//2)*4)%(10**9+7)))
