import sqlite3

connection = sqlite3.connect('C:\\Users\\ba2490\\Documents\\GitHub\\psi_sqlite3\\sqlite_database\\lol.db')
cursor = connection.cursor()
#
# Consulta à tabela "champions" para selecionar os campos "id_champion" e "nome_champion"
# onde o "nome_champion" é igual a "Akali".

cursor.execute('SELECT id_champion, nome_champion FROM champions WHERE nome_champion = "Akali"\n')
resultados = cursor.fetchall()
#
# Itera sobre os resultados e imprime cada registo encontrado.
#
for champions in resultados:
    print(champions)
#
# Consulta à tabela "roles" para selecionar os campos "id_role" e "nome_roles"
# onde o "nome_roles" é igual a "Mid".
#
#
# Itera sobre os resultados e imprime cada registo encontrado.
for roles in resultados:
    print(roles)

# Executa uma consulta para selecionar todos os campos e registos da tabela "champions".
cursor.execute('SELECT * FROM champions')

# Obtém todos os resultados da consulta anterior.
resultados = cursor.fetchall()

# Itera sobre os resultados e imprime cada registo encontrado.
for champions in resultados:
    print(champions)

# Guardar as alterações e fechar a conexão com a base de dados
connection.commit()
connection.close()