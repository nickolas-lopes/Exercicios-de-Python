def maior(a, b):
    return (a + b + abs(a - b))/2
x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)
maior1 = maior(x, y)
maior2 = maior(maior1, z)
print(f"{maior2:.0f} eh o maior")
