import sqlite3

connection = sqlite3.connect('C:\\Users\\ba2490\\Documents\\GitHub\\psi_sqlite3\\sqlite_database\\lol.db')
cursor = connection.cursor()

cursor.execute('''
                SELECT champions.id_champion, champions.nome_champion, champions.id_role, champions.id_build, roles.nome_role, builds.nome_build
                FROM champions
                INNER JOIN roles ON champions.id_role = roles.id_role
                INNER JOIN builds ON champions.id_build = builds.id_build
''')
resultaldos = cursor.fetchall()
for i in resultaldos:
    print(i)

connection.close()