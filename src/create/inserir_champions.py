import sqlite3

# Estabelecer conexão com a base de dados SQLite
connection = sqlite3.connect('C:\\Users\\ba2490\\Desktop\\psi_sqlite3_new\\psi_sqlite3\\sqlite_database\\lol.db')
cursor = connection.cursor()


num_champions = int(input("Quantos campeões você deseja adicionar? "))

# Inserir dados na tabela champions
for _ in range(num_champions):
    nome_champion = input("Digite o nome do campeão: ")
    
    # Mostrar as opções de roles e permitir que o usuário escolha
    cursor.execute('SELECT * FROM roles')
    roles = cursor.fetchall()
    print("Escolha o role para o campeão:")
    for i, role in enumerate(roles, start=1):
        print(f"{i}. {role[1]}")
    
    role_choice = int(input("Escolha o número do role: ")) - 1
    id_role = roles[role_choice][0]
    
    # Mostrar as opções de builds e permitir que o usuário escolha
    cursor.execute('SELECT * FROM builds')
    builds = cursor.fetchall()
    print("Escolha a build para o campeão:")
    for i, build in enumerate(builds, start=1):
        print(f"{i}. {build[1]}")
    
    build_choice = int(input("Escolha o número da build: ")) - 1
    id_build = builds[build_choice][0]
    
    # Inserir o campeão na tabela
    cursor.execute('INSERT INTO champions (nome_champion, id_role, id_build) VALUES (?, ?, ?)', 
                   (nome_champion, id_role, id_build))
    print(f"Campeão {nome_champion} adicionado com sucesso!\n")

# Guardar as alterações e fechar a conexão com a base de dados
connection.commit()
connection.close()