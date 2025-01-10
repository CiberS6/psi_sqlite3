import sqlite3

# Estabelecer conexão com a base de dados SQLite
connection = sqlite3.connect('C:\\Users\\ba2490\\Documents\\GitHub\\psi_sqlite3\\sqlite_database\\lol.db')
cursor = connection.cursor()

# Ler os valores da tabela champions por ordem alfabética
cursor.execute('SELECT * FROM champions ORDER BY nome_champion')
resultados = cursor.fetchall()

for i in resultados:
    print(i)

connection.close()