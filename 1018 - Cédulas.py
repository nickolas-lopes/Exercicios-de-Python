def main():
    valor_simbolico = input()
    valor = int(valor_simbolico)
    notas_100 = valor // 100
    valor = valor - notas_100 * 100
    notas_50 = valor // 50
    valor = valor - notas_50 * 50
    notas_20 = valor // 20
    valor = valor - notas_20 * 20
    notas_10 = valor // 10
    valor = valor - notas_10 * 10
    notas_5 = valor // 5
    valor = valor - notas_5 * 5
    notas_2 = valor // 2
    valor = valor - notas_2 * 2
    notas_1 = valor // 1
    print(f'{valor_simbolico}')
    print(f'{notas_100} nota(s) de R$ 100,00')
    print(f'{notas_50} nota(s) de R$ 50,00')
    print(f'{notas_20} nota(s) de R$ 20,00')
    print(f'{notas_10} nota(s) de R$ 10,00')
    print(f'{notas_5} nota(s) de R$ 5,00')
    print(f'{notas_2} nota(s) de R$ 2,00')
    print(f'{notas_1} nota(s) de R$ 1,00')
main()
