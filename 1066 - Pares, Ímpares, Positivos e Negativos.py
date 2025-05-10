def main():
    pares = 0
    impares = 0
    negativos = 0
    positivos = 0
    zero =0
    for i in range(0,5):
        n = int(input())
        if n % 2 == 0:
            pares += 1
        if n % 2 != 0:
            impares += 1
        if n < 0:
            negativos += 1
        else:
            positivos += 1
            if n == 0:
                positivos -= 1
    print(f'{pares} valor(es) par(es)')
    print(f'{impares} valor(es) impar(es)')
    print(f'{positivos} valor(es) positivo(s)')
    print(f'{negativos} valor(es) negativo(s)')
            
main()
