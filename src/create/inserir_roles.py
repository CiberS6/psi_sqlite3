import sqlite3

# Estabelecer conexão com a base de dados SQLite
connection = sqlite3.connect('C:\\Users\\ba2490\\Documents\\GitHub\\psi_sqlite3\\sqlite_database\\lol.db')
cursor = connection.cursor()

# Inserir dados predefinidos na tabela 'roles' (caso ainda não existam)
cursor.execute('INSERT INTO roles (nome_role) VALUES (?), (?), (?), (?), (?)', 
               ("TOP", "JUNGLE", "MID", "ADC", "SUPPORT"))

# Guardar as alterações e fechar a conexão com a base de dados
connection.commit()
connection.close()