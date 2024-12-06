# Projeto SQLite para gerir os Picks do League of Legends

Este projeto apresenta uma aplicação baseada em SQLite para gerir dados relacionados a campeões, funções (roles) e builds no League of Legends.

## Estrutura do Projeto

A estrutura do diretório é organizada da seguinte forma:

```
app/
├── main.py                  # Script principal que inicializa e interage com a base de dados
├── create/
│   ├── criar_tabelas.py      # Script para criar tabelas na base de dados
│   ├── inserir_builds.py      # Script para inserir dados na tabela 'builds'
│   ├── inserir_champions.py   # Script para inserir dados na tabela 'champions'
│   └── inserir_roles.py       # Script para inserir dados na tabela 'roles'
├── delete/
│   └── eliminar_champions.py # Script para excluir registros na tabela 'champions'
├── read/
│   └── ler_champions.py      # Script para ler dados da tabela 'champions'
├── sqlite_database/
│   └── lol.db               # Arquivo da base de dados SQLite
└── README.md                # Documentação do projeto
```

## Esquema da Base de Dados

A base de dados SQLite `lol.db` consiste nas seguintes tabelas:

1. **champions**
   - `id_champion` (INTEGER, Chave Primária)
   - `nome_champion` (TEXT, Obrigatório)
   - `id_role` (INTEGER, Chave Estrangeira para a tabela `roles`)
   - `id_build` (INTEGER, Chave Estrangeira para a tabela `builds`)

2. **roles**
   - `id_role` (INTEGER, Chave Primária)
   - `nome_role` (TEXT, Obrigatório)

3. **builds**
   - `id_build` (INTEGER, Chave Primária)
   - `nome_build` (TEXT, Obrigatório)

4. **picks** (ainda não definido no novo código, mas referenciado nos exemplos)
   - `id_pick` (INTEGER, Chave Primária)
   - `id_champion` (INTEGER, Chave Estrangeira para a tabela `champions`)
   - `id_role` (INTEGER, Chave Estrangeira para a tabela `roles`)

## Funcionalidades

- **Criação de tabelas:** Cria tabelas `champions`, `roles` e `builds` automaticamente, caso não existam.
- **Inserção de dados:** Permite adicionar registros manualmente em todas as tabelas.
- **Consulta de dados:** Realiza consultas SELECT para:
  - Buscar todos os picks para um campeão específico.
  - Obter detalhes de um campeão pelo nome.
  - Obter detalhes de uma função pelo nome.
  - Listar todos os campeões cadastrados.
- **Exclusão de dados:** Exclui registros específicos na tabela `champions`.

## Utilização

### Pré-requisitos

- Python 3.x instalado no sistema.
- Módulo SQLite3 (incluído por padrão na maioria das distribuições Python).

### Passos para Executar

1. Clone este repositório ou copie os ficheiros para o seu computador local.
2. Navegue até o diretório do projeto.
3. Execute o script principal para interagir com a base de dados:

   ```bash
   python app/main.py
   ```

### Scripts Individuais

- **`criar_tabelas.py`:** Cria as tabelas na base de dados.
- **`inserir_champions.py`:** Adiciona novos campeões com seus respectivos roles e builds.
- **`eliminar_champions.py`:** Exclui registros específicos da tabela `champions`.
- **`ler_champions.py`:** Realiza consultas na tabela `champions`.

## Exemplos de Consultas

Abaixo estão exemplos de consultas realizadas pelo script principal:

1. Buscar todos os picks para um campeão específico (`id_champion = 1`):
   ```sql
   SELECT id_pick, id_champion, id_role FROM picks WHERE id_champion = 1;
   ```

2. Obter detalhes de um campeão pelo nome (`nome_champion = "Akali"`):
   ```sql
   SELECT id_champion, nome_champion FROM champions WHERE nome_champion = "Akali";
   ```

3. Obter detalhes de uma função pelo nome (`nome_role = "Mid"`):
   ```sql
   SELECT id_role, nome_role FROM roles WHERE nome_role = "Mid";
   ```

4. Listar todos os campeões:
   ```sql
   SELECT * FROM champions;
   ```

## Alterar a Estrutura do Base de Dados

Se desejar modificar as tabelas ou realizar outras consultas, você pode editar os scripts existentes ou criar novos. Certifique-se de realizar backup antes de executar alterações significativas.

## Contribuições

Contribuições são bem-vindas! Por favor, abra uma *issue* ou envie um *pull request* se desejar sugerir melhorias ou adicionar novas funcionalidades.
