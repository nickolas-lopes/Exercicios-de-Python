n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
media = (n1 * 2 + n2 * 3 + n3 * 4 +  n4 * 1) / (2 + 3 + 4 + 1)
if media < 5:
    print(f"Media: {media:.1f}")
    print("Aluno reprovado.")
elif media >= 5 and media <= 6.9:
    print(f"Media: {media:.1f}")
    print("Aluno em exame.")
    exame = float(input())
    print(f"Nota do exame: {exame:.1f}")
    nova_nota = (exame + media) / 2
    if nova_nota >= 5:
        print("Aluno aprovado.")
        print(f"Media final: {nova_nota:.1f}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {nova_nota:.1f}")
else:
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")
