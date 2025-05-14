def main():
    i = 0
    n = int(input())
    while n > i:
        casos = int(input())
        if casos % 2 != 0 and casos < 0:
            print('ODD NEGATIVE')
        elif casos % 2 != 0 and casos > 0:
            print('ODD POSITIVE')
        elif casos % 2 == 0 and casos < 0:
            print('EVEN NEGATIVE')
        else:
            print('EVEN POSITIVE')
        i += 1
main()
