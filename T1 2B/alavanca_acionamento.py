# -*- coding: utf-8 -*-
"""Alavanca_Acionamento.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NoDREWLRla_dNaxiqgu-N8YfGq07GBHc
"""

'''classe alavanca de acionamento'''
class AlavancaAcionamento(object):
  '''Alavanca de acionamento'''
  def __init__(self):
    '''Construtor'''
    self.contador1 = 0
    self.contador2 = 0   

  def __del__(self):
    '''Destrutor'''
    print("removendo a alavanca: endereço {}".format(id(self)))

  def acionar(self):
    '''Acionando a alavanca'''
    self.contador1 += 1
  
  def relatorio(self):
    '''Relatório de agua'''
    print('Relatório de uso de água:')
    print('Número de descargas' + str(self.contador1))