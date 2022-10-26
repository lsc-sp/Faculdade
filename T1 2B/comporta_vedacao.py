# -*- coding: utf-8 -*-


"""comporta_vedacao.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1in5NDZbYdv27xhOD_Ng4ViCyqPzotZB4
"""

'''Classe Comporta de vedacao'''
class ComportaVedacao(object):
  '''Comporta de vedação'''
  
  def __init__(self):
    '''Método Construtor'''
    self.status = 'Desconhecido'

  def __del__(self):
    '''Método Destrutor'''
  
  def abrir(self):
    '''Abertura da comporta de vedacao '''
    self.status = 'ABERTA'
    print('Função de abrir comporta ativada')

  def fechar(self):
    '''Fechamento da comporta de vedação'''
    status = 'FECHADA'
    print('Função de fechar comporta ativada')

  def get_status(self):
    '''Status da comporta de vedação'''
    return self.status