import random
import time

def inputPositivo(userInput):
    if(userInput == 'sim' or userInput == 's'):
        return True
    else:
        return False

def inputNegativo(userInput):
    if(userInput == 'nao' or userInput == 'não' or userInput == 'n'):
        return True
    else:
        return False



def jogarNovamente():
    userInput = input('Deseja jogar o dado novamente? ').lower()
    if (inputPositivo(userInput)):
        jogarDado()
        jogarNovamente()
        return
    elif (inputNegativo(userInput)):
        print('Okay :)')
        return
    else:
        print('Resposta inválida')
        jogarNovamente()
        return


def jogarDado():
        print('Rodando dados...')
        time.sleep(2)
        print('O dado caiu no número: ', random.randint(1, 6))



def main():
    userInput = input('Você gostaria de jogar o dado? ').lower()
    if(inputPositivo(userInput)):
        jogarDado()
        jogarNovamente()
    elif(inputNegativo(userInput)):
        print('Okay :)')
        return
    else:
        print('Responsta inválida')
        main()


if __name__ == '__main__':
    main()


