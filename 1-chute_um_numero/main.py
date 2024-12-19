'''
CHUTE O NÚMERO
Objetivo: Criar um script que gerá um valor aleatoriamente, guardar este valor, 
e perguntar repetidamente para o usuário chutar o valor gerado até que ele acerte.

Habilidades praticas a aplicar:

-Random
-Comparadores matemáticos
-Controle de Fluxo
-Entrada de dados
-Saida de dados

Detalhes e boas Práticas: Você deve criar um projeto para rodar na linha de comando que ao iniciar,
irá gerar, armazenar, porem não exibir um valor aleatório entre um valor mínimo e máximo que será 
definido por você ( 10-100, por exemplo). Com esse valor gerado e armazenado de alguma forma que 
você (o criador ou jogador do script) não possa ver, faça uma pergunta do tipo: “Chute um número” 
para quem estiver rodando o script e com isso o programa deve gravar a resposta que foi passada.

Depois disso você terá 3 caminhos possíveis: 1. Avisar que a pessoa chutou baixo, 2 dizer que chutou
alto ou parabenizar dizer que acertou! Considerando os três possíveis caminhos que podem ser seguidos,
você deve cuidar para que em todo o momento a entrada de dados seja tratado para exceções e que caso 
o usuário digite algo inesperado, que ele receba uma mensagem amigável o informando das possíveis opções 
que seu programa oferece. Isso deve continuar acontecendo indefinitivamente até que a pessoa acerte o 
número ou desista por não conseguir acertar hahaha(acontece).
'''

import random
from time import sleep

def gerar_numero(min,max):
    numero_gerado = random.randint(min, max)
    return numero_gerado

def conferir_numero(numero_jogador, numero_gerado):
    if numero_jogador > numero_gerado:
        print('Chute um número menor 🔻')
        resultado = False
    elif numero_jogador < numero_gerado:
        print('Chute um número maior 🔺')
        resultado = False
    elif numero_jogador == numero_gerado:
        print('\nVocê acertou ✅')
        resultado = True
    return resultado

def menu():
    print('\nEscolha uma das seguintes opções: ')
    print('Jogar (1)')
    print('Sair (2)')
    

# programa principal
print('\n🍀 Olá, bem vindo ao jogo de acertar o número aleatório 🍀')
print('Qual o seu nome?')
nome = input('>> ')
print(f'\nOlá, {nome} 😁')
sleep(1)

while True:
    menu()
    tentativas_restantes = 10
    tentativa_usadas = 0
    try:
        escolha = int(input('>> '))
        if escolha == 1:
            print('\nOk, vou gerar um número aleatório entre 1 e 100, um momento...')
            for i in range (3):
                sleep(1)
                print('■□■□■□■□■□■□■□■□■')

            numero_gerado = gerar_numero(1,100)
            print('\nPronto, o número foi gerado 😎\n')
            # print(numero_gerado)
            print('Agora, tente acertar qual o número aleatório')
            sleep(1)
            while True:
                try:
                    palpite = int(input('>> '))
                    tentativa_usadas += 1
                    resposta = conferir_numero(palpite,numero_gerado)
                    if resposta == True:
                        print(f'Você usou {tentativa_usadas} tentativas 🤓')
                        break
                    else:
                        tentativas_restantes -= 1
                        if tentativas_restantes > 1:
                            print(f'Você tem {tentativas_restantes} tentativas')
                            continue
                        if tentativas_restantes == 1 and resposta == False:
                            print('Que pena, você perdeu 😥')
                    
                except:
                    print('Você precisa digitar um número ❗')

        elif escolha == 2:
             print('Ok, encerrando o programa 🤖')
             break

    except:
        print('Você precisa escolher entre Jogar(1) ou Sair(2) ❗')