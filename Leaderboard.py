from Imports import *
#abre o ficheiro e escreve os pontos que o jogador teve naquela partida e o nome
def EndGame():
    f = open("leaderboardpoints", "a")

    f.write("Nome"+"Points here")
    f.close()