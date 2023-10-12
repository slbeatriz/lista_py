numero = int(input("Digite um número: "))

print(f"Esses são os números ímpares até {numero}:")
for n in range(1, numero + 1, 2):
    print(n)