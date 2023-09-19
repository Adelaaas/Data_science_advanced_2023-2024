n, m, a, b = map(int, input().split())
a -= 1
b -= 1
field = []
for i in range(n):
    field.append(list(map(int, input().split())))
ans  = 0
for i in range(0, a+1):
    for j in range(0, b + 1):
        for x in range(a, n):
            for y in range(b, m):
                l = field[i][j] + field[x][y] + 2*(x - i + 1) + 2*(y - j + 1)
                if l > ans:
                    ans = l
print(ans)
