
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3 

while True:

   # Exibi o menu
   opcao = input(menu)


   # Opção Depósito
   if opcao == "d":
      valor = float(input("Informe o valor do depósito: "))

      if valor > 0:
         saldo += valor
         extrato += f"Depósito: R$ {valor:.2f}\n"
         print("Depósito realizado com sucesso!")
      else:
         print("Operação falhou! O valor informado é inválido.")

   # Opção Saque
   elif opcao == "s":
      valor = float(input("Informe o valor do saque: "))
      excedeu_saldo = valor > saldo
      excedeu_limite = valor > limite
      excedeu_saques = numero_saques >= LIMITE_SAQUES
      

      if excedeu_saldo:
         print("Operação falhou! Você não tem saldo suficiente.")

      elif excedeu_limite:
         print("Operação falhou! O valor de saque excede o limite.")

      elif excedeu_saques:
         print("Operação falhou! Número máximo de saques excedido.")

      elif valor > 0:
         saldo -= valor
         extrato += f"Saque: R$ {valor:.2f}\n"
         numero_saques += 1
         print("Saque realizado com sucesso!")
      else:
         print("Operação falhou! O valor informado é inválido.")

   # Opção Extrato
   elif opcao == "e":
      print("\n================ EXTRATO ================")
      print("Não foram realizadas movimentações." if not extrato else extrato)
      print(f"Saldo: R$: {saldo:.2f}")
      print("==========================================")

   # Opção Sair
   elif opcao == "q":
      print("Operação finalizada!")
      break
   
   # Opção Inválida
   else:
      print("Operação inválida, por favor selecione novamente a operação desejada.")
      