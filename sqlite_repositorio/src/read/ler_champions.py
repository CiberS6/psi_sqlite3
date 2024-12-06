import sqlite3

connection = sqlite3.connect('C:\\Users\\ba2490\Desktop\\tabelas_exercicio_new_new\\sqlite_database\\lol.db')
cursor = connection.cursor()

# Consulta à tabela "picks" para selecionar os campos "id_pick", "id_champion" e "id_role"
# onde o "id_champion" é igual a 1.
#
cursor.execute('SELECT id_pick, id_champion, id_role FROM picks WHERE id_champion = 1\n')
resultados = cursor.fetchall()
#
# Itera sobre os resultados e imprime cada registo encontrado.
#
for picks in resultados:
    print(picks)
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
cursor.execute('SELECT id_role, nome_roles FROM roles WHERE nome_roles = "Mid"')
resultados = cursor.fetchall()
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