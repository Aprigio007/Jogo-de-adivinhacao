#importando a funcão randint da biblioteca random para sortear o valor
from random import randint

#Pedir ao usuario o nome e guardar em uma variavel
nome_do_usuario = input('Ola! Qual é o seu nome? ')

#Sorteando o número
numero = randint(1, 100)
#Dar instrucões ao usuario
print(f'{nome_do_usuario}, Acabei de pensar em um número de 1 a 100. Consegur adivinhar? ')

#Iniciando a variavel para guardar as tentativas
numero_de_tentativas = 0

#Iniciando loop principal
while True:
    
    #Palpite do usuario
    palpite = int(input('--> '))
    
    #Adicionando a variavel de numero de tentativas mais um
    numero_de_tentativas += 1
    
    #Se o palpite for menor, imprimir "O número é maior!"
    if palpite < numero:
        print('O número é maior!')
       
     #Se o número for maior, imprimir "O número é menor"
    elif palpite > numero:
        print('O número é menor!')
        
     #Se o usuario acertar, imprimir uma mensagem de parabens   
    elif palpite == numero:
        
        #Perguntar se o usuario quer ir denovo
        ir_de_novo = input(f"PARABENS! voce conseguiu adivinhar em {numero_de_tentativas} tentativas! Quer ir outra rodada? [S/N]").upper()
        
        #Se a entrada for N, encerrar o loop de repeticao
        if ir_de_novo == "N":
            print('Adeus...')
            break
            
        #Se a entrada for S, sortear um novo numero com uma mensagem de instrucao    
        elif ir_de_novo == 'S':
            numero = randint(0, 100)
            print(f'{nome_do_usuario}, Acabei de pensar em um número de 1 a 100. Consegur adivinhar? ')
            