def main():
    i = 0
    soma_positivos = 0
    quant_positivos = 0
    while i < 6:
        n = float(input())
        if n > 0:
            soma_positivos += n
            quant_positivos += 1
        i += 1
    media = soma_positivos / quant_positivos
    print(f'{quant_positivos} valores positivos')
    print(f'{media:.1f}')
main()
