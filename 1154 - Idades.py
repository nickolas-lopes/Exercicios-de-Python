total = 0
a = int(input())
i = 0
while a > 0:
    if a > 0:
        total += a
    a = int(input())
    i += 1
print(f'{total/i:.2f}')
