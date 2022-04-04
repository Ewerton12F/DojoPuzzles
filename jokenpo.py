# https://dojopuzzles.com/problems/jokenpo/
#
# Jokenpo
#
# Jokenpo é uma brincadeira japonesa, onde dois jogadores escolhem um dentre 
# três possíveis itens: Pedra, Papel ou Tesoura.
# O objetivo é fazer um juiz de Jokenpo que dada a jogada dos dois jogadores 
# informa o resultado da partida.
# As regras são as seguintes:
# Pedra empata com Pedra e ganha de Tesoura
# Tesoura empata com Tesoura e ganha de Papel
# Papel empata com Papel e ganha de Pedra

player1 = str(input('Jogada do Player 1: '))
player2 = str(input('Jogada do Player 2: '))

if player1 == player2:
    print('Empate')
else: 
    if player1 == 'pedra':
        if player2 == 'tesoura':
            print('Player 1 ganhou')
            
        if player2 == 'papel':
            print('Player 2 ganhou')

    if player1 == 'tesoura':
        if player2 == 'pedra':
            print('Player 2 ganhou')
            
        if player2 == 'papel':
            print('Player 2 ganhou')
    
    if player1 == 'papel':
        if player2 == 'pedra':
            print('Player 1 ganhou')
            
        if player2 == 'tesoura':
            print('Player 2 ganhou')


