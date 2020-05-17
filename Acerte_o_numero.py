#Objetivo: criar um programa que gere um número aleatório e que me dê dicas para acertalo
#Em caso de erro debugar o codigo no VSCode

import random
import PySimpleGUI as sg


class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 10
        self.tentar_novamente = True

    def iniciar(self):
        #Layout
        layout = [
            [sg.Text('Chute um número de 1 a 10',size=(25,0))],  # 20 caracteres de largura e nenhum de altura
            [sg.Input(size=(18,0),key='ValorChute')],
            [sg.Button('Tentar!')],
            [sg.Output(size=(27,10))]   #Output é onde serão exibidos os dados
        ]
        #Criar a janela
        self.janela = sg.Window('Chute o numro!',layout=layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                #receber os valores
                self.evento,self.valores = self.janela.read()
                #fazer alguma coisa com esses valores
                if self.evento == 'Tentar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:  
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Tente um número mais baixo')
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Tente um valor mais alto')
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('Você acertou!')
                            break
        except:
            print('Favor digitar apenas números')
            self.iniciar()    
    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)
chute = ChuteONumero()
chute.iniciar()