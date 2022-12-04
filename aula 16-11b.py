#1 - Importar a biblioteca

import sqlite3

#2 -vamos estabelecer uma conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#3 - criar objeto do tipo cursor
cursor = conexao.cursor()

#4o. passo: comando para inserir um herói/vilão
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', 'Herói(na)')"


#5 executar o comando sql no sqlite
cursor.execute (sql)

#5 confirmar o insert com commit e fecha ro banco

conexao.commit()
conexao.close()