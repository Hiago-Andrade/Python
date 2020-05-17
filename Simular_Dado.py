# Simulador de um dado
# Simular o resultado de um dado no valor de 1 até 6

import random
import PySimpleGUI as sg


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Gostaria de gerar um novo valor ?'
        self.dado = True
        #Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'),sg.Button('Não')],
            [sg.Output(size=(30,10))],
        ]
        
    def Iniciar(self):
        #Janela
        self.janela = sg.Window('Simulador de Dado',layout=self.layout)
        #Ler os valores da tela
        try:
            while True:
                 self.eventos,self.valores = self.janela.Read()
                 if self.dado == True:
                        if self.eventos == 'Sim':
                            self.GerarValorDoDado()
                        else:
                            self.eventos == 'Não'
                            self.dado = False
                            print('')
                            print('OBRIGADO POR PARTICIPAR !')
        except:
            print('Ocorreu um erro na mensagem')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo)) 
        print(self.mensagem)         # Gerando um valor inteiro entre o valor minimo e o valor maximo
  
Simulador = SimuladorDeDado()        #Para usar uma classe temos que insatnciar ela 
Simulador.Iniciar()                                                                        

