

#1 - Importar a biblioteca

import sqlite3

#2 -vamos estabelecer uma conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#3 - criar objeto do tipo cursor
cursor = conexao.cursor()

#4 Comando SQL do banco

sql= " SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

#5 executar o comando sql no sqlite
cursor.execute (sql)

# 6 - exibir a consulta com todos os nomes de herois e vilões

pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)
  print("até agora tá OK")


for  pessoa  in  pessoas :
  print ( f"Nome: { pessoa [ 1 ] } ( { pessoa [ 3 ] } )" )
