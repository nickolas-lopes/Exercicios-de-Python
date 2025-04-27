cont = 1
maior = 0
posicao = 1
while cont <= 100:
    n = int(input())
    if n > maior:
        maior = n
        posicao = cont
    cont += 1
print(maior)
print(posicao)

