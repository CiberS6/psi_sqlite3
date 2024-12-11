import sqlite3

# Estabelecer conexão com a base de dados SQLite
connection = sqlite3.connect('C:\\Users\\ba2490\\Documents\\GitHub\\psi_sqlite3\\sqlite_database\\lol.db')
cursor = connection.cursor()

# Criar a tabela 'champions' caso ela ainda não exista
cursor.execute('''
                CREATE TABLE IF NOT EXISTS champions (
                id_champion INTEGER PRIMARY KEY AUTOINCREMENT, -- Chave primária autoincremental para os campeões
                nome_champion TEXT NOT NULL, -- Nome do campeão (campo obrigatório)
                id_role INTEGER NOT NULL, -- ID da role, ligado à tabela 'roles'
                id_build INTEGER NOT NULL -- ID da build, ligado à tabela 'builds'
                )               
                ''')

# Criar a tabela 'roles' caso ela ainda não exista
cursor.execute('''
                CREATE TABLE IF NOT EXISTS roles (
                id_role INTEGER PRIMARY KEY AUTOINCREMENT, -- Chave primária autoincremental para as roles
                nome_role TEXT NOT NULL -- Nome da role (campo obrigatório)
                )               
                ''')

# Criar a tabela 'builds' caso ela ainda não exista
cursor.execute('''
                CREATE TABLE IF NOT EXISTS builds (
                id_build INTEGER PRIMARY KEY AUTOINCREMENT, -- Chave primária autoincremental para as builds
                nome_build TEXT NOT NULL -- Nome da build (campo obrigatório)
                )               
                ''')

# Guardar as alterações e fechar a conexão com a base de dados
connection.commit()
connection.close()