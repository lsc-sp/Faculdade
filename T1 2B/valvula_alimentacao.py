# -*- coding: utf-8 -*-
"""valvula_alimentacao.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VN1wJHbNfa321ga86GAx6GCBrnJCje5_
"""

'''Valvula de alimentação'''

class ValvulaAlimentacao(object):
  '''Válvula de alimentação'''
  def __init__(self):
    '''Método Construtor'''
    self.capacidade_vazao = 2.0

  def __del__(self):
    '''Método Destrutor'''
    print("Removendo válvula de alimentação: Endereço {}".format(id(self)))

  def encher_agua(self):
    '''enchendo de agua'''
    print('Vazão: ' + str(self.capacidade_vazao) + " litros/seg")

  def get_vazao(self):
    '''Retorna a capacidade de vazao do vaso'''
    return self.capacidade_vazao
