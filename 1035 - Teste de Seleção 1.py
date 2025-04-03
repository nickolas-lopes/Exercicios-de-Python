def verifica(a, b, c, d):
    if b > c and d > a and c + d > a + b and (c and d) > 0 and a % 2 == 0:
        return "Valores aceitos"
    else:
        return "Valores nao aceitos"
a, b, c, d = input().split()
x = int(a)
y = int(b)
z = int(c)
n = int(d)
valor = verifica(x, y, z, n)
print(f"{valor}")
