import forca
import adivinhacao
import snake
from DoomPY import main

def escolhe_jogo():
    print("**************************************************")
    print("**********Bem vindo a central de jogos!!**********")
    print("**************************************************")
    
    print("(1) Jogo da Forca \n(2) Adivinhação\n(3) Snake\n(4) DOOM PY (Em desenvolvimento)\n")
    jogo = int(input("Qual você quer jogar?\n"))
    
    if(jogo == 1):
        print("Jogo da Forca - Selecionado!")
        forca.jogar()
    elif(jogo == 2):
        print("Jogo da Advinhação - Selecionado!")
        adivinhacao.jogar()
    elif(jogo == 3):
        print("Jogo da cobrinha - Selecionado!")
        snake.jogar()
    elif(jogo == 4):
        print('DOOM PY - Selecionado!')
        main.jogar()
        
if(__name__ == '__main__'):
    escolhe_jogo()