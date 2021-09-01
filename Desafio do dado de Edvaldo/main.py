from random import randint
from time import sleep


def receber_input(mensagem):
    user_input = input(mensagem).lower()
    if user_input == 'sim' or user_input == 's':
        return 'sim'
    elif user_input == 'não' or user_input == 'nao' or user_input == 'n':
        return 'nao'
    else:
        return 'invalido'


def jogar_dado():
    print('Jogando dados...')
    sleep(1)
    print('O dado caiu no número: ', randint(1, 6))
    jogar_dado_novamente()
    return


def jogar_dado_novamente():
    user_input = receber_input('Você quer jogar o dado novamente? ')
    if user_input == 'sim':
        jogar_dado()
        return
    elif user_input == 'nao':
        print('Okay :)')
        return
    else:
        print('Argumento inválido, tente novamente')
        jogar_dado_novamente()
        return


def main():
    user_input = receber_input('Você quer jogar o dado? ')
    if user_input == 'sim':
        jogar_dado()
        return
    elif user_input == 'nao':
        print('Okay :)')
        return
    else:
        print('Argumento inválido, tente novamente')
        main()


if __name__ == '__main__':
    main()
