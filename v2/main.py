from utils import menu, depositar, sacar, mostrar_extrato, cadastrar_cliente, cadastrar_conta, listar_contas


def main():
  LIMITE_DIARIO = 3
  AGENCIA = "0001"

  saldo = 0
  limite = 500
  numero_saques = 0
  extrato = ""
  usuarios = []
  contas = []
  
  while True:
    opcao = int(menu())

    #Exibir extrato  
    if opcao == 1: 
      extrato = mostrar_extrato(saldo, extrato=extrato)

    #Sacar
    elif opcao == 2:
      valor = float(input("Digite o valor do saque: "))
      
      saldo, extrato = sacar(saldo=saldo, 
                             valor=valor, 
                             extrato=extrato, 
                             limite=limite, 
                             numero_saques=numero_saques, 
                             limite_saques=LIMITE_DIARIO)
    
    #Depositar
    elif opcao == 3:
      valor = float(input("Digite o valor do deposito: "))
      
      saldo, extrato = depositar(saldo, valor, extrato)
    
    #Criar novo usuario
    elif opcao == 4:
      cadastrar_cliente(usuarios)
    
    #Criar nova conta
    elif opcao == 5:
      numero_conta = len(contas) + 1
      conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)

      if conta:    
        contas.append(conta)
    
    #Listar contas
    elif opcao == 6:
      listar_contas(contas)

    #Encerrar operação
    elif opcao == 0:
      print(f"Obrigado por usar o DioPyBank volte sempre")
      break

    else:
      print("Opção inválida, tente novamente")
      

main()

