def sacar(*, saldo: float, valor: float, extrato: str, limite: float, numero_saques: int, limite_saques: int):
  
  excedeu_saldo = saldo < valor

  excedeu_limite = limite < valor 
      
  excedeu_saque = numero_saques >= limite_saques

  if excedeu_saldo:
    print("\033[1;31m @@@ Por favor tente novamente, saldo insuficiente @@@ \033[m")

  elif excedeu_limite:
    print("\033[1;31m @@@ O valor do saque excedeu o limite permitido, tente novamente @@@ \033[m")

  elif excedeu_saque:
    print("\033[1;31m @@@ Limite de saques diarios excedidos, tente novamente amanha @@@ \033[m")

  elif valor > 0:
    saldo -= valor
    numero_saques += 1 
    extrato += f"Saque: R$ {valor:.2f}\n"
    print("\n\033[1;32m === Saque realizado com sucesso ===\033[m")

  else:
    print("\n\033[1;31m @@@ O valor do saque e invalido @@@ \033[m")

  return saldo, extrato

def depositar(saldo: float, valor: float, extrato: str):
  if valor > 0:
    saldo += valor
    extrato += f"Deposito: R$ {valor:.2f}\n"
    print("\n\033[1;32m === Deposito realizado com sucesso ===\033[m")
  
  else:
    print("\n\033[1;31m @@@ O valor do deposito e invalido, tente novamente. @@@\033[m")

  return saldo, extrato
  
def mostrar_extrato(saldo: float, /, *, extrato: str):
  if not extrato:
    extrato = f"""
    {"*"*10}EXTRATO{"*"*10}
    Nao foram realizadas movimentacoes

    \033[1;34mSaldo: R$ {saldo:.2f}\033[m
    {"*"*27}
    """
  else:
    extrato = f"""
    {"*"*10}EXTRATO{"*"*10}
    {extrato}
    \033[1;34mSaldo: R$ {saldo:.2f}\033[m
    {"*"*27}
    """

  return print(extrato)

def cadastrar_cliente(usuarios: list): 
  cpf = int(input("Digite o CPF do usuario (apenas numeros): "))
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print("\033[1;31m @@@ Usuario ja cadastrado @@@ \033[m")
    return

  nome = input("Digite o nome do usuario: ")
  data_nascimento = input("Digite a data de nascimento do usuario (dd-mm-aaaa): ")
  endereco = input("Informe o endereco (logradouro, numero - bairro - cidade/ sigla estado): ")
  
  usuarios.append({
    "nome": nome,
    "data_nascimento": data_nascimento,
    "cpf": cpf,
    "endereco": endereco
  })
  
  print("\033[1;32m === Usuario cadastrado com sucesso === \033[m")

def cadastrar_conta(agencia, numero_conta, usuarios):
  cpf = int(input("Digite o CPF do usuario (apenas numeros): "))
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print("\n\033[1;32m === Conta criada com sucesso!  === \033[m")
    return {
      "agencia": agencia,
      "numero_conta": numero_conta,
      "usuario": usuario
    }
  
  print("\n\033[1;31m @@@ Usuario nao encontrado, conta não pode ser criada @@@ \033[m")

def filtrar_usuario(cpf: int, usuarios: list):
  usuario_filtrado = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
  return usuario_filtrado[0] if usuario_filtrado else None

def listar_contas(contas: list):
  for conta in contas:
    informacoes = f"""
    Agencia: {conta['agencia']}
    C/C: {conta['numero_conta']}
    Titular: {conta['usuario']['nome']}
    """
    print(informacoes)
    print("*"*50)
    
def menu():
  menu = """
  Seja bem vindo ao banco DioPyBank

  Selecione a opcao desejada:
  [1] - Extrato
  [2] - Saque
  [3] - Deposito
  [4] - Novo usuario
  [5] - Nova conta
  [6] - Listar contas
  [0] - Sair
  
  Digite a opcao: """

  return input(menu)
