import sqlite3

# Estabelecer conexão com a base de dados SQLite
connection = sqlite3.connect('C:\\Users\\ba2490\\Desktop\\tabelas_exercicio_new_new\\sqlite_database\\lol.db')
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

# Inserir dados predefinidos na tabela 'roles' (caso ainda não existam)
cursor.execute('INSERT INTO roles (nome_role) VALUES (?), (?), (?), (?), (?)', 
               ("TOP", "JUNGLE", "MID", "ADC", "SUPPORT"))

# Inserir dados predefinidos na tabela 'builds' (caso ainda não existam)
cursor.execute('INSERT INTO builds (nome_build) VALUES (?), (?), (?), (?), (?), (?)', 
               ("AP", "AD", "LETHALITY", "BRUISER", "TANK", "SUPPORT"))

# Pedir ao utilizador quantos campeões deseja adicionar
num_champions = int(input("Quantos campeões você deseja adicionar? "))

# Ciclo para inserir os dados de cada campeão na tabela 'champions'
for _ in range(num_champions):
    nome_champion = input("Digite o nome do campeão: ")  # Obter o nome do campeão do utilizador
    
    # Mostrar as opções disponíveis na tabela 'roles'
    cursor.execute('SELECT * FROM roles')
    roles = cursor.fetchall()
    print("Escolha o role para o campeão:")
    for i, role in enumerate(roles, start=1):
        print(f"{i}. {role[1]}")  # Listar cada role com índice numérico
    
    # Obter a escolha do utilizador e associar ao ID correspondente
    role_choice = int(input("Escolha o número do role: ")) - 1
    id_role = roles[role_choice][0]
    
    # Mostrar as opções disponíveis na tabela 'builds'
    cursor.execute('SELECT * FROM builds')
    builds = cursor.fetchall()
    print("Escolha a build para o campeão:")
    for i, build in enumerate(builds, start=1):
        print(f"{i}. {build[1]}")  # Listar cada build com índice numérico
    
    # Obter a escolha do utilizador e associar ao ID correspondente
    build_choice = int(input("Escolha o número da build: ")) - 1
    id_build = builds[build_choice][0]
    
    # Inserir o novo campeão na tabela 'champions'
    cursor.execute('INSERT INTO champions (nome_champion, id_role, id_build) VALUES (?, ?, ?)', 
                   (nome_champion, id_role, id_build))
    print(f"Campeão {nome_champion} adicionado com sucesso!\n")

# Eliminar o registo na tabela "champions"
# onde o nome do campeão (nome_champion) é "Teemo".
# cursor.execute('DELETE FROM champions WHERE nome_champion = "Teemo"')

# Selecionar e verificar se ainda existe algum registo
# na tabela "champions" com o nome do campeão "Teemo".
# cursor.execute('SELECT * FROM champions WHERE nome_champion = "Teemo')


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
