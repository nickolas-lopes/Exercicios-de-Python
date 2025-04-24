n = int(input())
cont = 1
maior = 0
posicao = 1
while cont < 10:
    n = int(input())
    if n > maior:
        maior = n
    cont += 1
print(maior)

