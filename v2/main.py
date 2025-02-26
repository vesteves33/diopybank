#Primeira fase do projeto de sistema bancário consiste em implementar apenas 3 operações: depósito, saque e visualização do extrato da conta.
#Depoisito: Apenas adição de valores positivos para a conta, todos os depósitos precisam ficar armazenados em uma variavel e precisam ser exibidos no extrato.
#Saque: Pode ser permitido a realização de apenas 3 saques por dia com limite máximo de 500 reais por saque, não havendo saldo exibir mensagem ao usuario. Todas as operações armazenadas e exbidas no extrato
#Extrato: Exibir todas as operações realizadas na conta do usuário e o formato dos valores devem ser em R$ xxxx.xx


menu = """
  Seja bem vindo ao banco DioPyBank

  Selecione a opcao desejada:
  [1] - Extrato
  [2] - Saque
  [3] - Deposito
  [0] - Sair

"""


saldo = 0
limite = 500
numero_saque = 0
LIMITE_DIARIO = 3
extrato = ""


while True:
  
  opcao = int(input(menu))
  
  if opcao == 1:
    print(f"{"*"*10}EXTRATO{"*"*10}")
    print("Não foram realizadas movimentação" if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print(f"{"*"*27}")
    

  elif opcao == 2:
    valor = float(input("Digite o valor do saque: "))
    
    excedeu_saldo = saldo < valor

    excedeu_limite = limite < valor 
    
    excedeu_saque = numero_saque >= LIMITE_DIARIO
    
    if excedeu_saldo:
      print("Por favor tente novamente, saldo insuficiente")

    elif excedeu_limite:
      print("O valor do saque excedeu o limite permitido, tente novamente")

    elif excedeu_saque:
      print("Limite de saques diarios excedidos, tente novamente amanha")
    
    else:
      saldo -= valor
      numero_saque += 1
      extrato += f"Saque: R$ {valor:.2f}\n"
  
  elif opcao == 3:
    valor = float(input("Digite o valor do deposito: "))
    
    if valor > 0:
      saldo += valor
      extrato += f"Deposito: R$ {valor:.2f}\n"
    
    else:
      print("O valor do deposito e invalido, tente novamente")
  
  elif opcao == 0:
    print(f"Obrigado por usar o DioPyBank volte sempre")
    break

  else:
    print("Opção inválida")
    



