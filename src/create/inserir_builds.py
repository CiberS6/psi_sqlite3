import sqlite3

# Estabelecer conexão com a base de dados SQLite
connection = sqlite3.connect('C:\\Users\\ba2490\Desktop\\tabelas_exercicio_new_new\\sqlite_database\\lol.db')
cursor = connection.cursor()

# Inserir dados predefinidos na tabela 'builds' (caso ainda não existam)
cursor.execute('INSERT INTO builds (nome_build) VALUES (?), (?), (?), (?), (?), (?)', 
               ("AP", "AD", "LETHALITY", "BRUISER", "TANK", "SUPPORT"))

# Guardar as alterações e fechar a conexão com a base de dados
connection.commit()
connection.close()