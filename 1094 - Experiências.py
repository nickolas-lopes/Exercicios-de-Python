def main():
    qtdC = 1
    qtdR = 1
    qtdS = 1
    percC = qtdC / total_cob * 100
    percR = qtdR / total_cob * 100
    percS = qtdS / total_cob * 100
    total_cob = qtdC + qtdR + qtdS
    if qtdC and qtdR and qtdS == 1:
        qtdC, qtdR, qtdS = 0, 0, 0
    n = int(input())
    for i in range(n):
        qtd, cob = input().split()
        qtd = int(qtd)
        if cob == 'C':
            qtdC += qtd
        elif cob == 'R':
            qtdR += qtd
        elif cob == 'S':
            qtdS += qtd
    print(f'Total: {total_cob}')
    print(f'Total de coelhos: {qtdC}')
    print(f'Total de ratos: {qtdR}')
    print(f'Total de sapos: {qtdS}')
    print(f'Percentual de coelhos: {percC:.2f}')
    print(f'Percentual de ratos: {percR:.2f}')
    print(f'Percentual de sapos: {percS:.2f}')
main()
