import sqlite3

# Estabelecer conexão com a base de dados SQLite
connection = sqlite3.connect('C:\\Users\\ba2490\\Documents\\GitHub\\psi_sqlite3\\sqlite_database\\lol.db')
cursor = connection.cursor()

cursor.execute('''
                UPDATE champions
                SET id_champion = 49
                WHERE nome_champion = "Teemo"
                ''')

connection.commit()
connection.close()