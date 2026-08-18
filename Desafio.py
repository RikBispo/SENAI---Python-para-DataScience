dados  = {}



print('Cadastre-se:  ')


login = input('Login: ')
senha  = input('Senha: ') 


dados['login'] = login
dados['senha'] = senha  


print('dados cadastrados>>>', dados)




login_cad = input('Login: ')
senha_cad  = input('Senha: ') 


if login_cad == login and senha_cad == senha:
    print('Seja bem vindo  ao sistema Z')
    produtos = ['a','b','c']
    valores = [10.55,20.0,30.0]
else:
    print('Digite os dados corretamente...')    
carrinho = []
prod1 = input('Escolha o Primeiro Produto, das opções: a, b ou c: ')
if prod1 in produtos:
    carrinho.append (prod1)
else: print ('Digite um produto válido')
prod2 = input('Escolha o segundo produto, das opções: a, b ou c: ')
if prod2 in produtos:
    carrinho.append (prod2)
else: print ('Digite um produto válido')
prod3 = input('Escolha o Terceiro Produto, das opções: a, b ou c: ')
carrinho.append (prod3)
prod4 = input('Escolha o Quarto Produto, das opções: a, b ou c: ')
carrinho.append (prod4)
atotal=carrinho.count('a')
total_prod_a = atotal *  
total_prod_b =
total_prod_c = 
sum()