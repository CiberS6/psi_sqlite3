import sqlite3

# Estabelecer conexão com a base de dados SQLite
connection = sqlite3.connect('C:\\Users\\ba2490\\Documents\\GitHub\\psi_sqlite3\\sqlite_database\\lol.db')
cursor = connection.cursor()

cursor.execute('''
               CREATE TEMPORARY TABLE champions_temp AS,
               SELECT nome_champion, id_role, id_build,
               FROM champions,
               ORDER BY nome_champion
                ''')

cursor.execute('')

