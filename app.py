nome = input('Informe o seu Primeiro Nome: ')

if len(nome) <= 4:
    print(f'{nome.title()} Seu nome é curto.')
elif len(nome) >= 5 and len(nome) <=6:
    print(f'{nome.title()} Seu nome é normal.')
else:
    print(f'{nome.title()} Seu nome é muito grande.')
    