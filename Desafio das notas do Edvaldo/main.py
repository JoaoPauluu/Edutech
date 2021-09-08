# Função que pega um input de 4 números separados por espaço e transforma em uma lista
def entrada():
    entrada = input('Digite quatro notas de 0 a 10 separadas por um espaço: ').split()
    entrada2 = []
    for x in entrada:
        entrada2.append(int(x))

    return entrada2

# Função main
def main():
    notas = entrada()
    # Checa se todas as notas dentro do array são válidas
    for nota in notas:
        if (nota < 0) or (nota > 10):
            print('Uma das notas que você inseriu é inválida')
            break

    # Calcula a média e verifica se o aluno passou
    soma = sum(notas)
    media = soma / 4
    if (media < 6) and (media >= 4):
        print('Em recuperação')

    elif media < 4:
        print('Reprovado')

    elif media >= 6:
        print('Aprovado')

    # Mostra todas as notas e a média do aluno
    print(f'|{notas[0]}|{notas[1]}|{notas[2]}|{notas[3]} -> {media} -> Ednaldo Pereira best singer')


# Checa se o arquivo está ou não sendo importado como módulo para rodar o código
if __name__ == '__main__':
    main()
