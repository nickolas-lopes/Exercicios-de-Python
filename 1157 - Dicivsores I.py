def main():
    n = int(input())
    cont = 1
    while cont <= n:
        if n % cont == 0:
            print(f'{cont}')
        cont += 1
main()
