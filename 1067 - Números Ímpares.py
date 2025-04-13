x = int(input())
qtd = 1
while qtd < x:
    if x % 2 != 0:
        print(x)
        qtd -= 1
    x -= 1
