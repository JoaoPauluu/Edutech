from time import sleep

usuario_admin = False
fichas_usuario = 0
caixa_geral = 1000
jogos = {
    'Milho Verde': 0,
    'Sonho': 0,
    'Churrasquinho': 0,
    'Morango': 0,
    'Correio Elegante': 0,
    'Pebolim': 0,
    'Tiro ao Alvo': 0,
    'Fliperama': 0,
    'Cadeia': 0,
    'Pipoca': 0
}
jogos_lista = list(jogos.keys())

def space(number = 1):
    for i in range(number):
        print()

# Cabeçalho do terminal
def header():
    print('==========================================================')
    print('=== SISTEMA DE GERENCIAMENTO DE FICHAS MECATRON V. 420 ===')
    print('==========================================================')
    print()

# Função para entrar no sistema como Usuario ou Gerente
def login():
    global usuario_admin

    print('Entrar como:')
    print('       [0] Usuario (Comprar fichas e jogar jogos)')
    print('       [1] Gerente (Verificar estoque e mover as fichas')
    print('       [2] Sair')

    try:
        selecao = int(input('Seleção: '))
    except:
        print('Seleção inválida, tente novamente')
        return login()

    if selecao == 0:
        usuario_admin = False
        return
    elif selecao == 1:
        usuario_admin = True
        return
    elif selecao == 2:
        space(60)
        print('Obrigado por usar o meu programa :)')
        print('Manda uma key de mine ai edbaldos')
        sleep(2)
        exit()
    else:
        print('Seleção inválida, tente novamente')
        return login()

# Função para quando o usuario quiser comprar mais fichas
def comprar_fichas():
    global caixa_geral
    global fichas_usuario
    print(f'Quantas fichas você gostaria de comprar? Temos {caixa_geral} fichas no estoque')

    user_input = input('Quantidade: ')

    try:
        user_input = int(user_input)
    except:
        print('Você inseriu algum caractere invalido, tente novamente')
        space(5)
        return comprar_fichas()

    if user_input > caixa_geral:
        print('Infelizmente não temos tantas fichas assim :( Tente novamente com um número menor')
        space(5)
        return comprar_fichas()

    caixa_geral -= user_input
    fichas_usuario += user_input

    print('Realizando transação...')
    sleep(1)
    print('Compra realizada com sucesso :)')
    sleep(2)

    space(60)
    return user()

# Função para quando o usuario escolher algum jogo
def jogar(list_index):
    global jogos
    global jogos_lista
    global fichas_usuario

    jogo = jogos_lista[list_index]

    if fichas_usuario < 1:
        print('Você não tem fichas suficientes para jogar, compre mais fichas!')
        return user()

    print(f'Jogando {jogo}...')
    sleep(1)
    fichas_usuario -= 1
    print(f'Obrigado por ter jogado, espero que tenha se divertido :), seu total de fichas agora é de {fichas_usuario}')

    jogos[jogo] = jogos[jogo] + 1

    return user()

    

# Função quando a pessoa se registrar como Usuario
def user():
    global fichas_usuario
    global jogos_lista

    print(f'O que você gostaria de fazer? | Você tem {fichas_usuario} ficha(s)')
    print()
    print('Jogos disponíveis: ')
    for jogo in jogos:
        print(f'       [{jogos_lista.index(jogo)}] {jogo}')

    print('\nEstá sem fichas? Compre mais :)')
    print(f'       [{len(jogos_lista)}] Comprar fichas')

    print('\nCometeu algum erro?')
    print(f'       [{len(jogos_lista) + 1}] Voltar')

    user_input = input('Seleção: ')

    try:
        user_input = int(user_input)
    except:
        print('Você inseriu algum caractere invalido, tente novamente')
        space(5)
        return user()

    if user_input < len(jogos_lista):
        space(5)
        jogar(user_input)
    elif user_input == len(jogos_lista):
        space(5)
        comprar_fichas()
    elif user_input == len(jogos_lista) + 1:
        space(60)
        return main()

    return

# Função que mostra as fichas de todos os jogos e do caixa geral
def contar_fichas():
    global caixa_geral
    global jogos_lista
    global fichas_usuario
    global jogos

    print(f'Caixa Geral: {caixa_geral}')
    for jogo in jogos_lista:
        print(f'{jogo}: {jogos[jogo]}')
    
    print()
    print(f'Fichas com clientes: {fichas_usuario}')

    space(5)
    return admin()

# Função que move as fichas de um jogo para o caixa geral
def realocar_fichas():
    global jogos_lista
    global jogos
    global caixa_geral

    print('Qual jogo você gostaria de realocar as fichas (Mover as fichas do jogo para o Caixa Geral)?')

    for jogo in jogos_lista:
        print(f'       [{jogos_lista.index(jogo)}] {jogo}')

    print()
    print(f'       [{len(jogos_lista)}] Todos')

    user_input = input('Jogo: ')

    try:
        user_input = int(user_input)
    except:
        print('Você inseriu um caracter inválido, tente novamente')
        return realocar_fichas()

    if user_input > len(jogos_lista) or user_input < 0:
        print('Você inseriu um número inválido, tente novamente')
        space(5)
        return realocar_fichas

    if user_input == len(jogos_lista):
        total = 0
        for jogo in jogos_lista:
            caixa_geral += jogos[jogo]
            total += jogos[jogo]
            jogos[jogo] = jogos[jogo] - jogos[jogo]

        print(f'Fichas de todos os jogos movidas para a caixa geral (Total de fichas movidas: {total})')
        sleep(2)
        space(60)
        return admin()
    else:
        jogo = jogos_lista[user_input]
        caixa_geral += jogos[jogo]
        print(f'Movidas {jogos[jogo]} fichas de {jogo} para a Caixa Geral')
        jogos[jogo] = jogos[jogo] - jogos[jogo]
        return admin()



    



# Função para quando a pessoa se registrar como gerente
def admin():
    print('============================')
    print('=== MENU DE GERENCIAMENTO===')
    print('============================')

    print('O que você gostaria de fazer?')
    print('       [0] Contagem de fichas')
    print('       [1] Realocar fichas')
    print('       [2] Voltar')

    user_input = input('Seleção: ')

    try:
        user_input = int(user_input)
    except:
        print('Você inseriu algum caractere invalido, tente novamente')
        return admin()

    if user_input < 0 or user_input > 2:
        print('Você fez uma seleção inválida')
        return admin()

    if user_input == 0:
        space(20)
        contar_fichas()
    elif user_input == 1:
        space(20)
        realocar_fichas()
    elif user_input == 2:
        space(60)
        return main()

    return

# Função main()
def main():
    global usuario_admin

    header()
    login()
    
    if usuario_admin == False:
        space(20)
        user()
        return
    if usuario_admin == True:
        space(20)
        admin()
        return
    
    print('Falha no sistema (╯°□°）╯︵')
    return








# Checa se o arquivo está sendo importado como um módulo para depois rodá-lo
if __name__ == '__main__':
    main()
    input()

