#1 - Importar a biblioteca

import sqlite3

#passos 2 e 3 função conectar


def conectar():
  #2 -vamos estabelecer uma conexão com o banco de dados 
  conexao = sqlite3.connect("dc_universe.db")

  #3 - criar objeto do tipo cursor
  cursor = conexao.cursor()

  return conexao, cursor