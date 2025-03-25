def fatorial(n):
    resultado = 1
    while n > 1:
        resultado *= n
        n -= 1
    return resultado

print("Calculador de numero inteiro n>=1")
valor = int(input("Digite um numero > 0"))
res = fatorial()
print(res)