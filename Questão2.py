min_caracter = 6               # mínimo de 6 caracteres
min_dig = 0                    # mínimo 1 digito numeral
min_letra_min = 0              # mínimo 1 letra minuscula
min_letra_maiuscula = 0        # mínimo 1 letra maiuscula
min_caracter_especial = 0      # mínimo 1 caracter especial

senha = input('Digite sua senha: ')

if len(senha) >= min_caracter:
    for i in senha:
        if i.islower():
            min_letra_min += 1
        if i.isupper():
            min_letra_maiuscula += 1
        if i == '!' or i == '@' or i == '#' or i == '$' or i == '%' or i == '^' or i == '&' or i == '*' or i == '(' or i == ')' or i == '-' or i == '+':
            min_caracter_especial += 1
        if i.isdigit():
            min_dig += 1
        if min_dig >= 1 and min_letra_maiuscula >= 1 and min_letra_min >= 1 and min_caracter_especial >= 1:
            print('Senha válida')
else:
    if min_dig == 0:
        print('Faltou um número')
    if min_letra_min == 0:
        print('Faltou uma letra minuscula')
    if min_letra_maiuscula == 0:
        print('Faltou uma letra maiuscula')
    if min_caracter_especial == 0:
        print('Faltou um caracter especial')
        print('A senha precisa ter no mínimo 6 caracteres...')
