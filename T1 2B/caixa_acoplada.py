# -*- coding: utf-8 -*-
"""Caixa_Acoplada.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_VJi7dwVJxgdLHMnVVw4S2AwHZ2g-YL_
"""

''' classe caixa acoplada'''
from alavanca_acionamento import AlavancaAcionamento
from valvula_alimentacao import ValvulaAlimentacao 
from comporta_vedacao import ComportaVedacao

class CaixaAcoplada(object):

    def __init__(self):
        '''Método Construtor'''
        self.alavanca = AlavancaAcionamento()
        self.valvula = ValvulaAlimentacao()
        self.comporta = ComportaVedacao()
        self.nivel_maximo = 6.0
        self.nivel_agua = 0.0
        self.encher_caixa()
        print('Metodo Construtor da Caixa Acoplada')
    def __del__(self):
        '''Método Destrutor'''
        print("Removendo o Vaso Sanitário")

    def encher_caixa(self):
        '''Encher caixa da agua'''
        #self.comporta.abrir()
        self.comporta.fechar()
        statusComporta = self.comporta.get_status()
        print(self.comporta.get_status())
        
        if statusComporta == 'FECHADA':
            print("Encher a caixa d'a gua")
            while self.nivel_agua < self.nivel_maximo:
                self.nivel_agua = self.nivel_agua + 1
                if self.nivel_agua > self.nivel_maximo:
                    self.nivel_agua = self.nivel_maximo
            print("Nível de d'agua: " + str(round(self.nivel_agua,2))) 
        
        elif statusComporta == 'ABERTA':
            print('Comporta Aberta, não foi possível encher')
        
        else:
            print('Não foi possível acessar o status da comporta')

    def acionar(self,opcao):
        '''Acionar'''
        self.alavanca.acionar()
        self.comporta.abrir()
        self.comporta.fechar()
        self.valvula.encher_agua()
        self.encher_caixa()
    
        if opcao == 1:
            print('Acionamento 1 do vaso santinário')
            self.nivel_agua = 3
            print(f'Nivel de agua = {self.nivel_agua}')
        if opcao == 2:
            print("Acionamento 2 do vaso sanitário")
            self.nivel_agua = 0
            print(f'Nivel de agua = {self.nivel_agua}')

    def relatorio(self):
        '''Método para emitir relatorio de uso'''
        return self.alavanca.relatorio

    def statusDescarga(self):
        if self.nivel_agua > 0:
            print('Descarga feita e nivel de agua maior que zero')
        if self.nivel_agua == 0:
            print('Nível da agua zero')
