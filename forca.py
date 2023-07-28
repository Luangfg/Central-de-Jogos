def jogar():
    print("**************************************************")
    print("**********Bem vindo ao jogo da Forca!!************")
    print("**************************************************")
    
    
    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]
    
    enforcou = False
    acertou = False
    
    print(letras_acertadas)
    
    while(not enforcou and not acertou):
        chute = input("Qual letra?\n")
        chute = chute.strip()
        
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
                print("Encontrei a letra {} na posição {}\n".format(letra, index))
            index = index +1
        
        print(letras_acertadas)
    
    print("**Fim de jogo! **")
    
if(__name__ == "__main__"):
    jogar()
        