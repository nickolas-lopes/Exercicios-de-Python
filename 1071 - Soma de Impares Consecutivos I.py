def soma_impares_casos_A(a, b):
    soma = 0
    # Caso A seja ímpar e maior que B
    if a > b and a % 2 != 0:
        a -= 2  
        while a > b:
            soma += a
            a -= 2
            print(a)
        return soma

    # Caso A seja par e maior que B
    elif a > b and a % 2 == 0:
        a -= 1  
        while a > b:
            soma += a
            a -= 2
            print(a)
        return soma
def soma_impares_casos_B(a, b):
    soma = 0
    # Caso B seja ímpar e maior que A
    if b > a and b % 2 != 0: 
        b -= 2  
        while b > a:
            soma += b
            b -= 2
        return soma

    # Caso B seja par e maior que A
    elif b > a and b % 2 == 0:
        b -= 1  
        while b > a:
            soma += b
            b -= 2
        return soma
def numeros_iguais(a, b):
    return 0
a = int(input())
b = int(input())   
if a > b:
    soma = soma_impares_casos_A(a, b)
elif b > a:
    soma =  soma_impares_casos_B(a, b)
else:
    soma = numeros_iguais(a, b)
print(soma)

