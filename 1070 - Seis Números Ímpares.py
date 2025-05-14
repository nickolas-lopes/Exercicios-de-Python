def impares_consecutivos(x):
    for i in range(12):
        if x % 2 != 0:
            print(x)
        x += 1
        
def main():
    x = int(input())
    impares_consecutivos(x)
main()
