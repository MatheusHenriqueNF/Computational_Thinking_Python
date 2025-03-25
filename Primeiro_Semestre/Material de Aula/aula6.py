# a = input("Digita o primeiro numeor: ")
# b = input("Digita o segundo numeor: ")

# if a > b:
#     print("O primeiro número é maior.")
# elif a < b:
#     print("O segundo número é maior.")

# while a > b:
#     a = input("Digita o primeiro numeor: ")
#     b = input("Digita o segundo numeor: ")

#     if a > b:
#         print("O primeiro número é maior.")
#     elif a < b:
#         print("O segundo número é maior.")
mensagem = ""
while mensagem !="sair" or "SAIR":
    mensagem = input("Digite uma mensagem ou 'sair': ")
    if mensagem.lower() != "sair":
        print(f"Mensagem recebida: {mensagem}")
    else:
        print("Estou no else")
        break

print("Estou aqui fora do while")