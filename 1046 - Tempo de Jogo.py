def main():
    inicio, fim = input().split()
    inicio = int(inicio)
    fim = int(fim)
    # inicio < final
    if inicio < fim:
        horas_passadas = fim - inicio
        print(f'O JOGO DUROU {horas_passadas} HORA(S)')
    # inicio > final
    else:
        duracao = (24 - inicio) + fim
        print(f'O JOGO DUROU {duracao} HORA(S)')
main()
