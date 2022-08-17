a = int(input("Digite primeiro valor: "))
b = int(input("Digite segundo valor: "))
c = int(input("Digite terceiro valor: "))

if a < b and a < c:
    menor = a
elif b < c:
    menor = b
else:
    menor = c

print(f"MENOR = {menor}")