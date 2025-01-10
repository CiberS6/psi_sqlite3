import sqlite3

# Estabelecer conexão com a base de dados SQLite
connection = sqlite3.connect('C:\\Users\\ba2490\\Documents\\GitHub\\psi_sqlite3\\sqlite_database\\lol.db')
cursor = connection.cursor()

# Criar uma tabela temporária a partir da tabela champions e meter por ordem alfabética os valores da tabela
cursor.execute('''
               CREATE TEMPORARY TABLE champions_temp AS
               SELECT nome_champion, id_role, id_build
               FROM champions
               ORDER BY nome_champion
                ''')

# Eliminar os registos da tabela original
cursor.execute('DELETE FROM champions')

# Inserir os valores da tabela temporária na tabela original em ordem alfabética
cursor.execute(''' 
                INSERT INTO champions (id_champion, nome_champion, id_role, id_build)
                SELECT NULL, nome_champion, id_role, id_build
                FROM champions_temp;    
''')

# Eliminar a tabela temporária
cursor.execute('DROP TABLE champions_temp')
connection.commit()
connection.close()

