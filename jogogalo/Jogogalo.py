tabuleiro = [
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_']
    ]
historicoTab = []
ganhadores = []
ganhar = False
jogador1 = 'X'
jogador2 = 'O'




def menufuncao():
    while 1:
        print('PARA JOGAR DIGITE 1 ')
        print("PARA ENCERRAR DIGITE 0")
        opcao = int(input("Digite sua opção: "))
        if opcao == 1:
            limparTabuleiro()
            jogo()
        if opcao ==  0:
            print("Fim do jogo!")
            return 0



def jogo():
    
    while True:
        mostrarTabuleiro()
        inserirLinhaColuna(jogador1)

        if(checarSeGanhou(jogador1) == True):
            break
            
        mostrarTabuleiro()
        inserirLinhaColuna(jogador2)

        if(checarSeGanhou(jogador2) == True):
            break



def mostrarTabuleiro():
    for i in range(3):
        print("\n", tabuleiro[i][0],"|", tabuleiro[i][1],"|", tabuleiro[i][2],)



def inserirLinhaColuna(jogador):
    while 1:
        linha1 = int(input('JOGADOR '+ jogador+' | DIGITE A LINHA: '))
        coluna1 = int (input('JOGADOR '+ jogador+' | DIGITE A COLUNA: '))
        if  tabuleiro[linha1 - 1][coluna1 - 1] != 'O' or tabuleiro[linha1 - 1][coluna1 - 1] != 'X':
            break
    tabuleiro[linha1 - 1][coluna1 - 1] = jogador



def limparTabuleiro():
    for i in range(0,3):
        for j in range(0,3):
            tabuleiro[i][j] = '_'


def checarSeGanhou(jogador):
    velha = darVelha()
    linha =ganharEmLinha()
    coluna = ganharEmColuna()
    diagonal = ganharEmDiagonal()

    if(velha == True or linha == True or coluna == True or diagonal == True):
        mostrarTabuleiro()
        historicoTab.append(tabuleiro)
        return True


def ganharEmLinha():
    for i in range (3):
        if tabuleiro[i][0] == 'X' and tabuleiro[i][1] == 'X' and tabuleiro[i][2] == 'X':
            print('Jogador 1 Ganhou!')
            ganhadores.append("jogador 1 ganhou!")
            return True
            
        if tabuleiro[i][0] == 'O' and tabuleiro[i][1] == 'O' and tabuleiro[ai][2]== 'O':
            print('Jogador 2 Ganhou!')
            ganhadores.append("jogador 2 ganhou!")
            return True
        
    return False



def ganharEmColuna():
    for i in range (3):
        if tabuleiro[0][i] == 'X' and tabuleiro[1][i] == 'X' and tabuleiro[2][i] == 'X' :
            print('Jogador 1 Ganhou!')
            ganhadores.append("jogador 1 ganhou!")
            return True
                  
        if tabuleiro[0][i] == 'O' and tabuleiro[1][i] == 'O' and tabuleiro[2][i] == 'O' :
            print('Jogador 2 Ganhou!')
            ganhadores.append("jogador 2 ganhou!")            
            return True
    return False



def ganharEmDiagonal():
    if tabuleiro[0][0]== 'X' and tabuleiro[1][1]== 'X' and tabuleiro[2][2] == 'X':
        print ('Jogador 1 Ganhou!')
        ganhadores.append("jogador 1 ganhou!")
        return True
          
    if tabuleiro[0][2]== 'X' and tabuleiro[1][1]== 'X' and tabuleiro[2][0] == 'X':
        print ('Jogador 1 Ganhou!')
        ganhadores.append("jogador 1 ganhou!")
        return True
                  
    if tabuleiro[0][0]== 'O' and tabuleiro[1][1]== 'O' and tabuleiro[2][2] == "O":
        print ('Jogador 2 Ganhou!')
        ganhadores.append("jogador 2 ganhou!")
        return True
          
    if tabuleiro[0][2] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[2][0] == 'O':
        print('Jogador 2 Ganhou!')
        ganhadores.append("jogador 2 ganhou!")
        return True

    return False



def darVelha():
    if (tabuleiro[0][0] != '_' and tabuleiro[0][1] != '_'and tabuleiro[0][2] != '_'):
        if(tabuleiro[1][0] != '_' and tabuleiro[1][1] != '_' and tabuleiro[1][2] != '_'):
            if (tabuleiro[2][0] != '_' and tabuleiro[2][1] != '_' and tabuleiro[2][2] != '_'):
                if (ganharEmLinha() == False and ganharEmColuna() == False and ganharEmDiagonal() == False):
                    print ("# Deu velha #")
                    ganhadores.append("Velha")
                    return True
    return False



menufuncao()