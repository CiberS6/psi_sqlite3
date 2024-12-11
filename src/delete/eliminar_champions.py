import sqlite3

# Estabelecer conexão com a base de dados SQLite
connection = sqlite3.connect('C:\\Users\\ba2490\\Documents\\GitHub\\psi_sqlite3\\sqlite_database\\lol.db')
cursor = connection.cursor()

# Eliminar o registo na tabela "champions"
# onde o nome do campeão (nome_champion) é "Teemo".
cursor.execute('DELETE FROM champions WHERE nome_champion = "Teemo"')

# Selecionar e verificar se ainda existe algum registo
# na tabela "champions" com o nome do campeão "Teemo".
cursor.execute('SELECT * FROM champions WHERE nome_champion = "Teemo')

# Guardar as alterações e fechar a conexão com a base de dados
connection.commit()
connection.close()