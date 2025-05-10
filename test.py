def main():
    a, b = input().split()
    x, y = input().split()
    a = int(a)
    b = int(b)
    x = int(x)
    y = int(y)
    soma = x + y
    if a > b:
        a, b = b, a
        print(b - a)
    else:
        print(b - a)
    print(soma)
        
main()
    
