#Funcionalidades: - Adicionar transações (receitas e despesas) - Visualizar o saldo atual - Gerar um relatório de transações - Categorizar transações

#Estruturas de Dados: Utilize listas para armazenar as transações, onde cada transação é um dicionário contendo tipo (receita ou despesa), valor, categoria, e data. Dicionários podem ser usados para categorizar as transações e calcular totais por categoria.


def adicionar_transacao():
    respostaInicial = input("Deseja começar com um valor inicial na sua conta? (sim/não) ")

    if respostaInicial.lower() == 'sim':
        while True:
            try:
                valorInicial = float(input("Qual o valor inicial da sua conta? "))
                if valorInicial < 0:
                    print("Valor inicial inválido. Informe um valor positivo.")
                else:
                    print(f"O valor inicial da sua conta é: {valorInicial}")
                    break
            except ValueError:
                print("Erro: Você não digitou um número válido.")
    elif respostaInicial.lower() == 'não':
        valorInicial = 0
        print(f"Seu saldo atual é de: {valorInicial}")
    else:
        print("Resposta inválida. O programa será encerrado.")
        return

    while True:
        try:
            inserirValor = int(input("Deseja inserir um novo valor: 1 [SIM] ou 2 [NÃO]? "))

            if inserirValor == 1:
                respostaUsuario = int(input("Você deseja inserir uma: 1 [RECEITA] ou 2 [DESPESA]? "))

                if respostaUsuario == 1:
                    valor = float(input("Qual o valor da receita? "))
                    if valor < 0:
                        print("Valor inválido. Informe um valor positivo.")
                    else:
                        valorInicial += valor
                        print(f"Receita adicionada. Novo saldo: {valorInicial}")

                elif respostaUsuario == 2:
                    valor = float(input("Qual o valor da despesa? "))
                    if valor < 0:
                        print("Valor inválido. Informe um valor positivo.")
                    elif valorInicial >= valor:
                        valorInicial -= valor
                        print(f"Despesa adicionada. Novo saldo: {valorInicial}")
                    
                    else:
                        print("Saldo insuficiente. Transação recusada!")

                else:
                    print("Opção inválida. Informe 1 [RECEITA] ou 2 [DESPESA].")

            elif inserirValor == 2:
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida. Informe 1 [SIM] ou 2 [NÃO].")

        except ValueError:
            print("Erro: Você não digitou um número válido.")
    return valorInicial

adicionar_transacao()
    

<<<<<<< HEAD
def remover_transacao():
    pass
=======
def transacaoSaida():
     print("Olá, mundo")
>>>>>>> f9b2fea50f7e6b4adc82a531207f3426a308aadf

def saldoAtual():
    pass

def visualizar_relatorio():
    pass

def categorizarTransacoes():
    pass

def main():
    valorEntrada = transacaoEntrada()

if __name__ == "__main__":
    main()
