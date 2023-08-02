import random

#FUNÇÃO E CORPO DO JOGO FORCA
def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta("frutas.txt")
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)
    
    enforcou = False
    acertou = False
    erros = 0
        
    
    while(not enforcou and not acertou):  #LAÇO
        chute = pede_chute()
        
        if(chute in palavra_secreta):        
           marca_chute_correto(chute, letras_acertadas , palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)  #QUANTIDADE DE TENTATIVAS E ERROS
        
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    
    if(acertou):
        imprime_mensagem_ganhador()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
        
    print("**Fim de jogo! **")


#-----------------------------------------FUNÇÕES E MENSAGEM -------------------------------------------------
#-------ERROS DO JOGADOR
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")
    
    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        
    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")
        
    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")
        
    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")
        
    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")
        
    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")
        
    if(erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
        
    print(" |            ")
    print("_|___         ")
 
 
#-------MENSAGEM DO GANHADOR
def imprime_mensagem_ganhador():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
        
        
#-------MENSAGEM DO PERDEDOR
def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
 


#-------COLOCA A LETRA DO CHUTE NA POSIÇÃO CORRETA 
def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index +=1   
        

#-------INICIALIZA A FUNÇÃO PARA INSERUR UMA LETRA PARA O CHUTE
def pede_chute():
    chute = input("Qual letra?\n")
    chute = chute.strip().upper()
    return chute
    
#-------INICIALIZA A PALAVRA SECRETA COM "_"
def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


#-------MENSAGEM DE BOAS VINDAS NO JOGO
def imprime_mensagem_abertura():
    print("**************************************************")
    print("**********Bem vindo ao jogo da Forca!!************")
    print("**************************************************")   


#-------INICIALIZAÇÃO DA PALAVRA SECRETA
def carrega_palavra_secreta(primeira_linha_valida=5, nome_arquivo="palavras.txt"):
    #ABRE O ARQUIVO QUE CONTEM OS NOMES DE FRUTA
    arquivo = open(nome_arquivo, "r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


if(__name__ == "__main__"):
    jogar()
    