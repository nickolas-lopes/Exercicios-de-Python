x = int(input())
y = int(input())


if x > y:
    x, y = y, x

soma = 0
atual = x + 1  

while atual < y:
    if atual % 2 != 0:
        soma += atual
    atual += 1

print(soma)
