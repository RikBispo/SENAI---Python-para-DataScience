pe = input('Deseja acessar o banco? ')
if pe != 'sim':
   exit()
else:
    senha  =  input('Senha')
    if  senha  == '123':
        saldo = 3000
        extrato = []
        funcionar = 1
        while funcionar == 1:

            print('banco X')
            print('''Menu:
                  
                1 - saque
                2 - deposito
                3 - extrato
                4 - sair 
                ''')
            op =  input('\nescolha a operação: ')
            if op == '4':
                funcionar = 0
            if  op == '1':
                print('seu saldo é de ',saldo)
                saque = float(input ('Quando gostaria de sacar?'))
                if saque <= saldo:
                    saldo = saldo - saque
                    print('\nFoi sacado ', saque, 'totalizando o saldo de: ', saldo,'em sua conta')
                    extrato.append (f'Saque - {saque}')
                else:
                    print('Saldo Insuficiente! \n')
                    print('Saldo atual', saldo)
            if op == '2':
                    print('Quanto gostaria de Depositar?')
                    print('Saldo atual ', saldo)
                    deposito = float(input('R$: '))
                    if deposito > 0:
                        saldo = saldo + deposito
                        print('Seu saldo atual é: ', saldo)
                        extrato.append (f'Deposíto: + {deposito}')
                    else:
                        print('Não é possível depositar um valor negativo ou igual a zero')
            if op == '3':
                    print('saldo: ', saldo)
                    print('\n Operações realizadas no dia:\n')
                    print(extrato)
    else:
        print('senha incorreta, tente novamente')            







       


